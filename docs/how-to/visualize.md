# Visualize Your Protocol

Preview your ReproSchema protocols and activities as interactive web forms.

## Goal

Test and preview your schemas in a real user interface before deployment.

## Try It Now!

Want to see ReproSchema in action? Click below to view our demo protocol:

[**🚀 View Demo Protocol**](https://www.repronim.org/reproschema-ui/#/?url=https://raw.githubusercontent.com/ReproNim/reproschema-demo-protocol/main/reproschema_demo_protocol/reproschema_demo_protocol_schema)

This demo includes various question types and branching logic to showcase ReproSchema capabilities.

## Prerequisites

- A valid ReproSchema protocol or activity
- Web browser
- Internet connection (for hosted UI)

## Quick Start

### Using the Hosted UI

Visit the ReproSchema UI with your schema URL:

```
https://www.repronim.org/reproschema-ui/#/?url=YOUR_SCHEMA_URL
```

Replace `YOUR_SCHEMA_URL` with the direct link to your schema file.

## Step-by-Step Guide

### 1. Prepare Your Schema URL

#### For GitHub-Hosted Schemas

1. Navigate to your schema file on GitHub
2. Click the "Raw" button
3. Copy the raw URL

**Example:**
- GitHub URL: `https://github.com/ReproNim/reproschema-demo-protocol/blob/main/reproschema_demo_protocol/reproschema_demo_protocol_schema`
- Raw URL: `https://raw.githubusercontent.com/ReproNim/reproschema-demo-protocol/main/reproschema_demo_protocol/reproschema_demo_protocol_schema`

#### For Local Development

Use a local server:

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

Then use: `http://localhost:8000/path/to/schema.jsonld`

### 2. Construct the Preview URL

Combine the base UI URL with your schema:

```
https://www.repronim.org/reproschema-ui/#/?url=https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO/main/path/to/schema.jsonld
```

### 3. Open and Test

1. Open the constructed URL in your browser
2. Navigate through your protocol
3. Test all interactions and branching logic

## Advanced Options

### URL Parameters

Add additional parameters to customize the preview:

```
https://www.repronim.org/reproschema-ui/#/
  ?url=YOUR_SCHEMA_URL
  &lang=es              # Language (en, es, fr, etc.)
```

### Running UI Locally

For development, run the UI locally:

```bash
git clone https://github.com/ReproNim/reproschema-ui
cd reproschema-ui
npm install
npm run serve
```

Then access at `http://localhost:8080`

## Troubleshooting

### Schema Doesn't Load

**Problem:** Blank screen or loading spinner

**Solutions:**
1. **Check URL encoding** - Ensure special characters are encoded
2. **Verify raw URL** - Must be direct file access, not GitHub page
3. **Validate schema first** - Run validation before visualization
4. **Check browser console** - Look for error messages

### CORS Errors

**Problem:** "Cross-Origin Request Blocked"

**Solutions:**
1. Use GitHub raw URLs (they include CORS headers)
2. Host on a server with proper CORS configuration
3. Use local development server

### Missing Activities

**Problem:** Protocol loads but activities are missing

**Solutions:**
1. Check activity paths in protocol schema
2. Ensure all referenced files are accessible
3. Use absolute URLs for external activities

## Common Issues and Solutions

### 1. Slow Loading

- Optimize schema file size
- Host schemas on fast CDN
- Minimize external dependencies

### 2. Mobile Display

- Test responsive layout
- Check touch interactions
- Verify keyboard accessibility

## Next Steps

- [Validate your schemas](validation.md) before visualization
- [Create a protocol](create-protocol.md) to visualize
- [Use library assessments](use-library-assessments.md) in your protocol

!!! note "Future Updates"

    This guide will be updated when reproschema-ui or reproschema-server receive major updates. The demo protocol link will always showcase the latest features.
