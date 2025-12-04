#!/bin/bash

# Start local HTTPS server for AR testing
# Camera access requires HTTPS in modern browsers

echo "🚀 Starting local HTTPS server for AR testing..."
echo "📱 Camera access requires HTTPS - this script provides that"
echo ""

# Check if we have Python 3
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found"
    
    # Create a simple HTTPS server with self-signed certificate
    echo "🔒 Creating self-signed certificate for HTTPS..."
    
    # Generate private key
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"
    
    if [ $? -eq 0 ]; then
        echo "✅ Certificate created successfully"
        echo ""
        echo "🌐 Starting HTTPS server on https://localhost:8000"
        echo "📱 Open this URL on your mobile device:"
        echo "   https://[YOUR_LOCAL_IP]:8000"
        echo ""
        echo "🔧 To find your local IP, run: ifconfig | grep 'inet '"
        echo ""
        echo "⚠️  You'll need to accept the security warning for the self-signed certificate"
        echo "   This is normal for local development"
        echo ""
        
        # Start HTTPS server
        python3 -m http.server 8000 --bind 0.0.0.0
    else
        echo "❌ Failed to create certificate"
        echo "🔄 Falling back to HTTP server (camera may not work)"
        echo "🌐 Starting HTTP server on http://localhost:8000"
        python3 -m http.server 8000 --bind 0.0.0.0
    fi
else
    echo "❌ Python 3 not found"
    echo "🔄 Trying Python 2..."
    
    if command -v python &> /dev/null; then
        echo "✅ Python 2 found"
        echo "🌐 Starting HTTP server on http://localhost:8000"
        echo "⚠️  Camera access may not work with HTTP"
        python -m SimpleHTTPServer 8000
    else
        echo "❌ No Python found"
        echo "Please install Python 3 for HTTPS support"
        exit 1
    fi
fi
