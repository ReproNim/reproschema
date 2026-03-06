# Backup Strategies

Protect your protocol data with robust backup systems.

## Goal

Ensure your ReproSchema data is safe, recoverable, and accessible when needed.

## Prerequisites

- Deployed protocol
- Basic understanding of system administration

## Backup Types

### 1. Schema Backups

#### Why Important
- Protects your intellectual property
- Enables version rollback
- Facilitates collaboration

#### Implementation
```bash
# Daily schema backups
0 2 * * * cd /path/to/reproschema && \
  tar -czf backups/schemas_$(date +\%Y\%m\%d).tar.gz protocols/ activities/ items/

# Keep last 30 days
0 3 * * * find /path/to/backups/ -name "schemas_*.tar.gz" -mtime +30 -delete
```

#### Version Control
```bash
# Git as backup
cd /path/to/reproschema
git add .
git commit -m "Daily backup: $(date)"
git push origin main
```

### 2. Response Data Backups

#### Database Backups
```bash
# PostgreSQL backup
0 1 * * * pg_dump -U username dbname > backups/db_$(date +\%Y\%m\%d).sql

# Compress and encrypt
gzip backups/db_$(date +\%Y\%m\%d).sql
gpg --encrypt --recipient you@example.com backups/db_$(date +\%Y\%m\%d).sql.gz
```

#### Export Backups
```bash
# Daily JSON export
0 1 * * * docker exec reproschema-server python manage.py \
  export_responses --output-dir ./backups/$(date +\%Y\%m\%d)
```

### 3. Configuration Backups

```bash
# Backup environment and config files
tar -czf backups/config_$(date +\%Y\%m\%d).tar.gz \
  .env docker-compose.yml nginx.conf
```

## Backup Storage Strategies

### 3-2-1 Rule

1. **3 copies** of your data
2. **2 different types** of storage media
3. **1 offsite** copy

#### Local Storage
```bash
# Local NAS or external drive
rsync -avz /path/to/backups/ /mnt/backup/nas/
```

#### Cloud Storage
```bash
# AWS S3
aws s3 sync /path/to/backups/ s3://reproschema-backups/ \
  --storage-class GLACIER

# Google Cloud Storage
gsutil rsync -r /path/to/backups/ gs://reproschema-backups/

# Backblaze B2
b2 upload-file reproschema-backups backups/latest.tar.gz latest.tar.gz
```

#### Offsite
- Sync to home server
- Physical hard drive rotation
- Geographic distribution

## Backup Automation

### Backup Script
```bash
#!/bin/bash
# backup.sh - Automated backup script

DATE=$(date +%Y%m%d)
BACKUP_DIR="/path/to/backups"
RETENTION_DAYS=30

# Create backup directory
mkdir -p $BACKUP_DIR/$DATE

# Backup schemas
tar -czf $BACKUP_DIR/$DATE/schemas.tar.gz protocols/ activities/ items/

# Backup database
docker exec postgres pg_dump -U user dbname > $BACKUP_DIR/$DATE/db.sql

# Backup config
tar -czf $BACKUP_DIR/$DATE/config.tar.gz .env docker-compose.yml

# Upload to cloud
aws s3 sync $BACKUP_DIR/$DATE s3://reproschema-backups/$DATE/

# Cleanup old backups
find $BACKUP_DIR/ -type d -mtime +$RETENTION_DAYS -exec rm -rf {} \;

# Log completion
echo "Backup completed: $DATE" >> /var/log/backup.log
```

### Cron Schedule
```bash
# crontab -e
0 1 * * * /path/to/backup.sh
```

## Recovery Procedures

### Schema Recovery
```bash
# Extract from backup
tar -xzf backups/schemas_20260306.tar.gz

# Restore to correct location
rsync -av protocols/ /path/to/reproschema/protocols/
```

### Database Recovery
```bash
# Restore PostgreSQL
psql -U username dbname < backups/db_20260306.sql

# Or restore specific table
psql -U username dbname -f backups/db_20260306.sql
```

### Full System Recovery
```bash
# 1. Restore schemas
tar -xzf backups/schemas_latest.tar.gz

# 2. Restore database
psql -U username dbname < backups/db_latest.sql

# 3. Restore configuration
tar -xzf backups/config_latest.tar.gz

# 4. Restart services
docker-compose down
docker-compose up -d
```

## Testing Backups

### Regular Testing
```bash
# Monthly backup test
#!/bin/bash
BACKUP_DATE="20260306"
TEST_DIR="/tmp/reproschema_test_$BACKUP_DATE"

# Extract backup
mkdir -p $TEST_DIR
tar -xzf backups/schemas_$BACKUP_DATE.tar.gz -C $TEST_DIR

# Validate schemas
reproschema validate $TEST_DIR/protocols/*.jsonld

# Test database restore
createdb test_restore
psql -U username test_restore < backups/db_$BACKUP_DATE.sql

# Report results
echo "Backup test completed: $BACKUP_DATE" | mail -s "Backup Test" admin@example.com
```

### Verification Checklist
- [ ] Schemas validate successfully
- [ ] Database restores without errors
- [ ] Configuration files are intact
- [ ] Services start correctly
- [ ] Data is accessible

## Monitoring

### Backup Alerts
```bash
# Check if backup exists today
if [ ! -f "backups/db_$(date +\%Y\%m\%d).sql" ]; then
    echo "Backup failed: $(date)" | mail -s "Backup Alert" admin@example.com
fi
```

### Storage Monitoring
```bash
# Check disk space
df -h | grep -vE '^Filesystem|tmpfs|cdrom'
```

### Integrity Checks
```bash
# Verify backup checksums
md5sum backups/*.tar.gz > checksums.md5
md5sum -c checksums.md5
```

## Security Considerations

### Encryption
```bash
# Encrypt backups
gpg --encrypt --recipient admin@example.com backup.tar.gz

# Store public key for decryption
# Keep private key secure offline
```

### Access Control
```bash
# Restrict backup directory permissions
chmod 700 /path/to/backups/
chown root:root /path/to/backups/
```

### Audit Logging
```bash
# Log all backup operations
echo "$(date): Backup operation by $USER" >> /var/log/backup.log
```

## Disaster Recovery Plan

### 1. Immediate Response
- Assess damage extent
- Notify stakeholders
- Activate recovery procedures

### 2. Data Recovery
- Restore from most recent good backup
- Validate data integrity
- Update documentation

### 3. Service Restoration
- Restart services in priority order
- Monitor for errors
- Test critical functionality

### 4. Post-Incident Review
- Document incident
- Update procedures
- Train team

## Best Practices

1. **Automate**: Use cron for scheduled backups
2. **Test regularly**: Verify backups monthly
3. **Monitor**: Set up alerts for failures
4. **Document**: Keep recovery procedures updated
5. **Encrypt**: Protect sensitive data
6. **Diversify**: Use multiple storage locations
7. **Retain**: Keep backups for required period

## Troubleshooting

### Backup Fails
- Check disk space
- Verify permissions
- Review logs

### Restore Fails
- Validate backup integrity
- Check schema version compatibility
- Review database logs

### Space Issues
- Implement retention policy
- Compress backups
- Archive old data

## Next Steps

- [Monitor system health](monitoring-guide.md)
- [Set up alerting](deploy-protocol.md)
