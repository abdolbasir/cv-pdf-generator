# wkhtmltopdf Installation Guide for Windows

## Step 1: Download wkhtmltopdf
1. Go to: https://wkhtmltopdf.org/downloads.html
2. Download the Windows installer (64-bit) - it should be named something like `wkhtmltopdf-0.12.6-1.msvc2015-win64.exe`

## Step 2: Install wkhtmltopdf
1. Run the downloaded installer
2. Follow the installation wizard
3. **Important**: Install to the default location (`C:\Program Files\wkhtmltopdf\`)
4. Make sure to check "Add to PATH" during installation

## Step 3: Verify Installation
1. Open Command Prompt or PowerShell
2. Run: `wkhtmltopdf --version`
3. You should see version information if installed correctly

## Step 4: Test PDF Generation
1. Start your Django development server
2. Navigate to a profile detail page
3. Click the "Generate PDF" button
4. The PDF should download automatically

## Troubleshooting

### If you still get "No wkhtmltopdf executable found":
1. **Check if wkhtmltopdf is installed**:
   - Open Command Prompt
   - Type: `wkhtmltopdf --version`
   - If this fails, wkhtmltopdf is not in your PATH

2. **Add to PATH manually**:
   - Open System Properties → Advanced → Environment Variables
   - Add `C:\Program Files\wkhtmltopdf\bin` to the PATH variable
   - Restart your terminal/IDE

3. **Restart your Django server** after making PATH changes

### Alternative: Use Chocolatey (if you have it installed)
```bash
choco install wkhtmltopdf
```

### Alternative: Use Scoop (if you have it installed)
```bash
scoop install wkhtmltopdf
```

## Notes
- The updated code will automatically detect wkhtmltopdf in common installation locations
- If you install to a custom location, update the `possible_paths` list in `views.py`
- Make sure to restart your Django development server after installing wkhtmltopdf 