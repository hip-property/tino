# Run gitlab scripts locally

Gitlab runner exec is deprecated and very slow.

There is a current issue tracking a potential new tool:
https://gitlab.com/gitlab-org/gitlab-runner/issues/2797#note_51070788 

## Third party options investigates

1. Potential tool but needs bash 
https://gitlab.com/ercom/citbx4gitlab
2. Runs the job in a docker container
https://gitlab.com/snippets/1683314
Could be modified to run in a shell

### Setup
```
ln -s /Users/stephenavery/dev/home/tino/src/exec.py /usr/local/bin/tino
mv _tino ~/.oh-my-zsh/completions
```
