# python-playsounds

tiny script to play a nice collection of sounds

## startup hook

use [`pm2`](https://pm2.io/docs/runtime/guide/installation/) to start the `run.py` script on boot

```sh
pm2 start run.py --name playsounds
pm2 save
pm2 startup
pm2 save
```

to restart the script use

```sh
pm2 restart playsounds
```
