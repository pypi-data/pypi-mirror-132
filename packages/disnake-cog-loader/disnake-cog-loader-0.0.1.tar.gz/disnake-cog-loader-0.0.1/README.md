# How to use

The first step is to let the extension know which class is the cog.
Suppose the cog subclass is defined as `FooCog`,
```py
class FooCog(commands.Cog):
    pass
```

You should name the file, `foo_cog.py`

The module will then convert snake_case to PascalCase and then try to import the cog to load it.
The module will try to pass the bot instance to it so be sure to accept it in the constructor,

```py
class FooCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        ...
```

`disnake.ext.loader.Loader` accepts two parameters, `bot` and `folder_name`.

- `bot`
    - The `commands.Bot` instance to load cogs.
- `folder_name`
    - The folder where the cogs are located. You may also enter something like `ext.cogs` if the cogs folder is inside a folder named `ext`.
