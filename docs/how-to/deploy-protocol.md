# Deploy Your Protocol

Deploy your validated ReproSchema protocol for data collection.

## Goal

Make your protocol accessible to participants through various deployment options.

## Prerequisites

- Validated ReproSchema protocol
- Chosen deployment platform
- Basic understanding of web hosting

## Deployment Options

### Option 1: GitHub Pages (Free)

**Best for:** Small studies, proof of concepts, testing

#### Steps

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add protocol for deployment"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository settings
   - Scroll to "Pages" section
   - Select "Deploy from a branch"
   - Choose "main" branch

3. **Access Your Protocol**
   ```
   https://www.repronim.org/reproschema-ui/#/?url=https://YOUR_USERNAME.github.io/YOUR_REPO/protocols/protocol_schema.jsonld
   ```

### Option 2: Reproschema-Server (Recommended)

**Best for:** Production studies, data collection, full features

#### Using Docker

1. **Clone reproschema-server**
   ```bash
   git clone https://github.com/ReproNim/reproschema-server
   cd reproschema-server
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Deploy with Docker**
   ```bash
   docker-compose up -d
   ```

4. **Upload Your Protocol**
   - Access admin interface
   - Upload protocol files
   - Configure study settings

### Option 3: Custom Hosting

**Best for:** Custom integrations, institutional hosting

#### Requirements

- Web server (Apache, Nginx)
- HTTPS support
- CORS headers configured

#### Steps

1. **Upload Protocol Files**
   ```bash
   scp -r protocols/ user@your-server:/var/www/html/
   ```

2. **Configure CORS**
   Add to your server config:
   ```apache
   Header always set Access-Control-Allow-Origin "*"
   Header always set Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS"
   ```

3. **Test Access**
   ```
   https://www.repronim.org/reproschema-ui/#/?url=https://your-domain.com/protocols/protocol_schema.jsonld
   ```

## Configuration Options

### Study Settings

Configure study parameters in your protocol:

```json
{
    "@context": "https://raw.githubusercontent.com/ReproNim/reproschema/1.0.0/contexts/reproschema",
    "@type": "reproschema:Protocol",
    "@id": "my_study_protocol",
    "prefLabel": "My Research Study",
    "description": "Description of the study",
    "landingPage": {
        "@id": "README.md",
        "@language": "en"
    },
    "ui": {
        "allow": [
            "reproschema:AutoAdvance",
            "reproschema:AllowExport",
            "reproschema:DisableBack"
        ]
    }
}
```

### Access Control

#### Public Access
No additional configuration needed.

#### Restricted Access
Use authentication parameters:

```json
{
    "ui": {
        "allow": [
            "reproschema:RequireAuth"
        ],
        "authConfig": {
            "type": "token",
            "endpoint": "https://your-auth-server.com/validate"
        }
    }
}
```

### Data Collection

#### Local Storage (Testing)
Data stored in browser localStorage.

#### Server Storage (Production)
Configure data endpoint:

```json
{
    "ui": {
        "dataEndpoint": "https://your-server.com/api/responses"
    }
}
```

## Pre-Deployment Checklist

### Technical Validation

- [ ] All schemas validate successfully
- [ ] Protocol renders correctly in reproschema-ui
- [ ] All activities and items load properly
- [ ] Branching logic works as expected
- [ ] Required fields are marked correctly

### Content Review

- [ ] All text is proofread and accurate
- [ ] Instructions are clear and complete
- [ ] Consent forms are legally compliant
- [ ] Contact information is correct
- [ ] Study information is complete

### Testing

- [ ] Test complete participant flow
- [ ] Test on different devices (desktop, mobile, tablet)
- [ ] Test in different browsers
- [ ] Test with different languages (if applicable)
- [ ] Verify data export/storage

### Security & Privacy

- [ ] HTTPS enabled
- [ ] Data encryption configured
- [ ] Privacy policy accessible
- [ ] GDPR/HIPAA compliance verified
- [ ] Backup systems in place

## Monitoring and Maintenance

### Analytics

Track study progress:
- Participation rates
- Completion rates
- Drop-off points
- Technical issues

### Updates

For schema updates during data collection:
1. Create new version of schema
2. Test thoroughly
3. Deploy to staging environment
4. Migrate to production
5. Update participant links

### Data Management

Regular tasks:
- Export collected data
- Backup data securely
- Monitor storage capacity
- Review data quality

## Troubleshooting

### Protocol Won't Load

**Check:**
- Schema validation passes
- All file paths are correct
- CORS headers are present
- HTTPS is enabled

### Data Not Saving

**Check:**
- Data endpoint configuration
- Server permissions
- Network connectivity
- Storage capacity

### Performance Issues

**Solutions:**
- Optimize schema file sizes
- Use CDN for hosting
- Minimize external dependencies
- Enable compression

## Post-Deployment

### Participant Communication

Provide participants with:
- Direct protocol URL
- Instructions for technical requirements
- Contact information for support
- Estimated completion time

### Data Collection

Monitor:
- Response rates
- Data quality
- Technical issues
- Participant feedback

## Best Practices

1. **Start Small**: Test with small groups before full deployment
2. **Version Control**: Use semantic versioning for protocols
3. **Documentation**: Keep deployment documentation updated
4. **Security**: Regular security audits and updates
5. **Backup**: Multiple backup strategies
6. **Monitoring**: Continuous monitoring of all systems

## Next Steps

- [Set up data analysis pipeline](../tutorials/analyzing-data.md)
- [Configure automated backups](backup-strategies.md)
- [Monitor study progress](monitoring-guide.md)