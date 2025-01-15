FROM apache/superset

# Install additional packages
COPY docker/superset/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy configurations
COPY config/superset/superset_config.py /app/pythonpath/
COPY assets/branding/ /app/superset/static/assets/
COPY assets/css/ /app/superset/static/css/

# Initialize script
COPY docker/scripts/init-superset.sh /app/init-superset.sh
RUN chmod +x /app/init-superset.sh

EXPOSE 8088
CMD ["/app/init-superset.sh"]
