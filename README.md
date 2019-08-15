# Trello CLI

Config files for a joat based cli, you don't know what is joat? 😱
get your shit together and go [read about joat!](https://github.com/sennav/joat)

## Instalation

```
joat install sennav/trello.joat
```

Or just clone this repo in your home folder with under the folder `.trello.joat` and create a symlink in your path name `trello` pointing to your `joat` binary.

## Usage

It's used like a regular CLI, here's the help with the commands:

```
trello 0.0.1 (joat 0.0.2)
Vinicius <senna.vmd@gmail.com>
Trello CLI

USAGE:
    trello [SUBCOMMAND]

FLAGS:
    -h, --help       Prints help information
    -V, --version    Prints version information

SUBCOMMANDS:
    auto_complete           Create auto complete script
    board                   print board situation
    board_details           get board
    card_id_by_substring    get card id by name substring (returns first match)
    cards                   get cards
    checklists              get board checklists
    edit_card               edit a card
    help                    Prints this message or the help of the given subcommand(s)
    list_id_by_substring    get list id by name substring (returns first match)
    lists                   get board lists
    move                    Move card to a list
    new                     Create new card at the TODO column
    new_card                create a new card

```

## Config

You need to set the following environment variables:
* `TRELLO_KEY` - API key, google how to get one :)
* `TRELLO_TOKEN` - API token, google how to get one :)
* `TRELLO_BOARD_ID` - optionally you can define a default board to work on.
