from .nolinks import NoLinks


async def setup(bot):
    await bot.add_cog(NoLinks(bot))
