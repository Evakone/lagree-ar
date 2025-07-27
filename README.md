# AR Mural Demo

An AR mural application built with A-Frame and MindAR for marker-based augmented reality.

## Local Testing

### HTTP (Basic)
```bash
python3 -m http.server 8000
```
Access: http://localhost:8000

### HTTPS (Recommended for AR)
```bash
# Certificates are already generated
python3 -c "import http.server, ssl, socketserver; handler = http.server.SimpleHTTPRequestHandler; httpd = socketserver.TCPServer(('', 8443), handler); httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', keyfile='key.pem', server_side=True); print('HTTPS server running on https://localhost:8443'); httpd.serve_forever()"
```
Access: https://localhost:8443

## Free Hosting Options

### Netlify (Recommended)
1. Go to [netlify.com](https://netlify.com)
2. Drag and drop this folder to deploy
3. Your site will be live with HTTPS automatically

### GitHub Pages
1. Create a GitHub repository
2. Push this code to the repository
3. Enable GitHub Pages in repository settings
4. Select "Deploy from a branch" and choose main/master

### Vercel
1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repository or drag and drop
3. Deploy automatically with HTTPS

## Testing on Mobile

1. **Same WiFi Network**: Use your computer's IP address
2. **Public Hosting**: Use the provided URL from Netlify/Vercel/GitHub Pages
3. **HTTPS Required**: AR features need HTTPS to work properly

## Files Structure
- `index` - Main HTML file
- `assets/` - 3D models and assets
- `targets.mind` - MindAR marker file
- `cert.pem` & `key.pem` - SSL certificates for local HTTPS

## Marker Image
Make sure you have the marker image that corresponds to `targets.mind` for testing the AR functionality. 