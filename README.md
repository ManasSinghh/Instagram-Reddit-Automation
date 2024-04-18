<h1 align="center">
  Instagram-Reddit Automation
</h1>

<h4 align="center">
    A simple automation script that posts images from Reddit to Instagram.
 </h4>

 <p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://i.imgur.com/6ogFiV3.png)

## Key Features

- Fetches images from Reddit
- Posts images to Instagram
- Customizable settings
- Easy to use
- Easy Automation using GitHub Actions
- Use any subreddit

## How To Use

You can either run the script locally or use GitHub Actions to automate the process.

### Local

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/yashraj-n/Instagram-Reddit-Automation

# Go into the repository
$ cd Instagram-Reddit-Automation

# Install dependencies

$ pip install -r requirements.txt
```

Rename `.env.example` to `.env` and fill in the required details.

Get Upstash Redis URL from [here](https://upstash.com/)

OPTIONAL: You can also use Sentry for error tracking. Get the DSN from [here](https://sentry.io/)

Run the script

```bash
# Run the app
$ python main.py
```

### GitHub Actions

1. Fork this repository

2. Go to the repository settings and add the following secrets

```bash

INSTA_USERNAME - Your Instagram Username
INSTA_PASSWORD - Your Instagram Password
SUBREDDIT - The subreddit you want to fetch images from
UPSTASH_REDIS_REST_URL - Upstash Redis URL
UPSTASH_REDIS_REST_TOKEN - Upstash Redis Token
SENTRY_URL - Sentry DSN (Optional)

```

3. Go to the Actions tab and enable workflows

4. You can also customize the schedule in `.github/workflows/Automate.yml`

## Credits

This repo uses [subzeroid/instagrapi](https://github.com/subzeroid/instagrapi)'s api for posting images to Instagram.

## License

[MIT](LICENSE)

