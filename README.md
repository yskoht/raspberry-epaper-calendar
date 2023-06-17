# Raspberry e-paper calendar

![IMG_0470](https://github.com/yskoht/raspberry-epaper-calendar/assets/34795067/3d5f02d0-a3af-4d29-a201-06a0840fe6d2)

## Prepare

```sh
pip install raspberry-epaper
```

```sh
apt install imagemagick
```

```sh
git clone https://github.com/yskoht/raspberry-epaper-calendar.git /pic
```

```sh
crontab -l
1 0 * * * /bin/sh /pic/run.sh >>error.log 2>&1
```

### Run

```sh
sh /pic/run.sh
```

