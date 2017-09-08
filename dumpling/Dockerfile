FROM debian:stretch

# Follow the cookbook to make the dumpling!
COPY docker-build /srv/
RUN /srv/docker-build

# Enable git pull rebase autostash.
COPY gitconfig /etc/

# Serve the chopsticks.
# Use an entrypoint script to add users from host to the container.
COPY docker-entrypoint /usr/local/bin/
ENTRYPOINT ["docker-entrypoint"]
CMD ["bash"]
