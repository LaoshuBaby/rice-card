# rice-card

A Open Graph image preview card generater written in Python.

## Feature

* Template based, can change style fastly.
* Built-in variables that let you fast combine with what you need.

## Alternative

### local-host

* [wei/socialify](https://github.com/wei/socialify)
* [DGP-Studio/Snap.Hutao.Docs.Open.Graph](https://github.com/DGP-Studio/Snap.Hutao.Docs.Open.Graph)

### SaaS

* [Vercel/og-image](https://github.com/vercel/og-image) Note: this repository had been archived, and now serve as function on Vercel.
* [BannerBear](https://www.bannerbear.com/)
* [dito.so](https://www.dito.so/)

## Why this name?

~~Because I cooked rice today.~~

There are very few projects with the same name, so it is not easy to cause confusion. There are only 2 projects with the same name on GitHub: [azuremine/RiceCardMageSys](https://github.com/azuremine/RiceCardMageSys) and [luckrf/Ricecard](https://github.com/luckrf/Ricecard).

## Q&A

Q: Which Pain Point you solve?

A: 1. For organization they may want to generate unified preview image style for every repository, while there isn't a workflow for those kind of batch task.
   1. GitHub's default preview image can't work correct with CJK characters.
   2. Current Socialify mainly intent for git repository, but many website (especially those built with wordpress) can't use it.
   3. You can use it preview osmcha changeset when share a link in Telegram or Discord.

Q: Where are colour defined?

A: Colour value are extracted from [github-linguist/linguist](https://github.com/github-linguist/linguist/blob/master/lib/linguist/languages.yml)
