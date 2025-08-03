# views.py
import io
import pdfkit 
from django.conf import settings
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from django.db import transaction

from .models import ProfileModel, Education
from .forms import ProfileForm, EducationForm, EducationFormSet


class ProfileCreateView(CreateView):
    model = ProfileModel
    form_class = ProfileForm
    template_name = 'pdf/profile_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['education_formset'] = EducationFormSet(self.request.POST, prefix='education')
        else:
            context['education_formset'] = EducationFormSet(prefix='education')
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        education_formset = context['education_formset']
        
        if self.request.method == 'POST':
            if education_formset.is_valid():
                self.object = form.save()
                education_formset.instance = self.object
                education_formset.save()
            else:
                return self.render_to_response(self.get_context_data(form=form))
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile_detail', kwargs={'pk': self.object.pk})

class ProfileDetailView(DetailView):
    model = ProfileModel
    template_name = 'pdf/profile_detail.html'
    context_object_name = 'profile' 

def generate_pdf(request, pk):
    """Generate PDF from profile detail page"""
    profile = get_object_or_404(ProfileModel, pk=pk)
    
    # Render the template to HTML
    template = loader.get_template('pdf/profile_detail.html')
    html_content = template.render({'profile': profile})
    
    # Configure pdfkit options for better compatibility
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None,
        'disable-smart-shrinking': None,
        'print-media-type': None,
        'no-stop-slow-scripts': None,
        'javascript-delay': '1000',
        'load-error-handling': 'ignore'
    }
    
    try:
        # Try to configure wkhtmltopdf path for Windows
        import os
        wkhtmltopdf_path = None
        
        # Common Windows installation paths
        possible_paths = [
            r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe',
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                wkhtmltopdf_path = path
                break
        
        # Create pdfkit configuration
        if wkhtmltopdf_path:
            config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
            pdf = pdfkit.from_string(html_content, False, options=options, configuration=config)
        else:
            # Try without explicit path (if it's in PATH)
            pdf = pdfkit.from_string(html_content, False, options=options)
        
        # Ensure we have valid PDF content
        if not pdf or len(pdf) < 100:  # Basic check for valid PDF
            raise Exception("Generated PDF is too small or empty")
        
        # Create HTTP response with proper headers for download
        response = HttpResponse(pdf, content_type='application/pdf')
        
        # Clean filename for better compatibility
        safe_filename = "".join(c for c in profile.name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_filename = safe_filename.replace(' ', '_')
        
        # Set proper headers for download
        response['Content-Disposition'] = f'attachment; filename="{safe_filename}_CV.pdf"'
        response['Content-Length'] = len(pdf)
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        return response
        
    except Exception as e:
        # Handle pdfkit errors (e.g., wkhtmltopdf not installed)
        error_message = str(e)
        if "No wkhtmltopdf executable found" in error_message:
            return HttpResponse(
                "Error: wkhtmltopdf is not installed. Please install it from https://wkhtmltopdf.org/downloads.html",
                status=500
            )
        else:
            return HttpResponse(f"Error generating PDF: {error_message}", status=500)

def generate_pdf_alternative(request, pk):
    """Alternative PDF generation method with better download handling"""
    profile = get_object_or_404(ProfileModel, pk=pk)
    
    # Render the template to HTML
    template = loader.get_template('pdf/profile_detail.html')
    html_content = template.render({'profile': profile})
    
    # Configure pdfkit options for better compatibility
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None,
        'disable-smart-shrinking': None,
        'print-media-type': None,
        'no-stop-slow-scripts': None,
        'javascript-delay': '1000',
        'load-error-handling': 'ignore',
        'quiet': None
    }
    
    try:
        # Try to configure wkhtmltopdf path for Windows
        import os
        import tempfile
        wkhtmltopdf_path = None
        
        # Common Windows installation paths
        possible_paths = [
            r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe',
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                wkhtmltopdf_path = path
                break
        
        # Create a temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as html_file:
            html_file.write(html_content)
            html_file_path = html_file.name
        
        try:
            # Create pdfkit configuration
            if wkhtmltopdf_path:
                config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
                pdf = pdfkit.from_file(html_file_path, False, options=options, configuration=config)
            else:
                # Try without explicit path (if it's in PATH)
                pdf = pdfkit.from_file(html_file_path, False, options=options)
            
            # Ensure we have valid PDF content
            if not pdf or len(pdf) < 100:  # Basic check for valid PDF
                raise Exception("Generated PDF is too small or empty")
            
            # Create HTTP response with proper headers for download
            response = HttpResponse(pdf, content_type='application/pdf')
            
            # Clean filename for better compatibility
            safe_filename = "".join(c for c in profile.name if c.isalnum() or c in (' ', '-', '_')).rstrip()
            safe_filename = safe_filename.replace(' ', '_')
            
            # Set proper headers for download
            response['Content-Disposition'] = f'attachment; filename="{safe_filename}_CV.pdf"'
            response['Content-Length'] = len(pdf)
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            
            return response
            
        finally:
            # Clean up temporary HTML file
            try:
                os.unlink(html_file_path)
            except:
                pass
                
    except Exception as e:
        # Handle pdfkit errors (e.g., wkhtmltopdf not installed)
        error_message = str(e)
        if "No wkhtmltopdf executable found" in error_message:
            return HttpResponse(
                "Error: wkhtmltopdf is not installed. Please install it from https://wkhtmltopdf.org/downloads.html",
                status=500
            )
        else:
            return HttpResponse(f"Error generating PDF: {error_message}", status=500) 

def test_pdf_generation(request, pk):
    """Test view to debug PDF generation issues"""
    profile = get_object_or_404(ProfileModel, pk=pk)
    
    try:
        import os
        import subprocess
        
        # Test if wkhtmltopdf is available
        wkhtmltopdf_path = None
        possible_paths = [
            r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
            r'C:\wkhtmltopdf\bin\wkhtmltopdf.exe',
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                wkhtmltopdf_path = path
                break
        
        # Test wkhtmltopdf version
        if wkhtmltopdf_path:
            try:
                result = subprocess.run([wkhtmltopdf_path, '--version'], 
                                      capture_output=True, text=True, timeout=10)
                version_info = result.stdout.strip()
            except Exception as e:
                version_info = f"Error running wkhtmltopdf: {str(e)}"
        else:
            version_info = "wkhtmltopdf not found in common locations"
        
        # Test PATH
        try:
            result = subprocess.run(['wkhtmltopdf', '--version'], 
                                  capture_output=True, text=True, timeout=10)
            path_version = result.stdout.strip()
        except Exception as e:
            path_version = f"wkhtmltopdf not in PATH: {str(e)}"
        
        debug_info = f"""
        <h2>PDF Generation Debug Info</h2>
        <p><strong>Profile:</strong> {profile.name}</p>
        <p><strong>wkhtmltopdf Path:</strong> {wkhtmltopdf_path or 'Not found'}</p>
        <p><strong>Version (from path):</strong> {version_info}</p>
        <p><strong>Version (from PATH):</strong> {path_version}</p>
        <p><strong>Current working directory:</strong> {os.getcwd()}</p>
        <p><strong>Python executable:</strong> {os.sys.executable}</p>
        """
        
        return HttpResponse(debug_info, content_type='text/html')
        
    except Exception as e:
        return HttpResponse(f"Debug error: {str(e)}", status=500) 