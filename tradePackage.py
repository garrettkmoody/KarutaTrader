import discord

class TradePackage:
    def __init__(self, price, card, askerName = "No user selected", bidderName = "No user selected"):
        self.bidderName = bidderName
        self.askerName = askerName
        self.bidderUser = None
        self.askerUser = None
        self.price = price
        self.card = card
        self.venmo = None
        self.link = None

    def get_bidderName(self):
        return self.bidderName
    def get_askerName(self):
        return self.askerName
    def get_bidderUser(self):
        return self.bidderUser
    def get_askerUser(self):
        return self.askerUser
    def set_bidderName(self, newName):
        self.bidderName = newName
    def set_askerName(self, newName):
        self.askerName = newName
    def set_bidderUser(self, newUser):
        self.bidderUser = newUser
    def set_askerUser(self, newUser):
        self.askerUser = newUser

    def get_embed(self, stage=1):
        if stage == 1:
            embedVar = discord.Embed(title="Trade Outline", color=0xFF9900)
            embedVar.add_field(name=self.askerName, value="***PRICE*** : `${}`".format(self.price), inline=False)
            embedVar.add_field(name=self.bidderName, value="***CARD*** : `{}`".format(self.card), inline=False)
        elif stage == 2:
            embedVar = discord.Embed(title="Trade Completion `(1/2)`", color=0xFF00FF)
            embedVar.add_field(name = self.bidderName, value = "➡️", inline = True)
            embedVar.add_field(name = '`Task`', value = "Send $`{}` to this link {}".format(self.price, self.link), inline = True)
            embedVar.add_field(name = 'Status', value = "❌", inline = True)
        elif stage == 3:
            embedVar = discord.Embed(title="Trade Completion `(2/2)`", color=0xFF00FF)
            embedVar.add_field(name =self.askerName, value= "➡️", inline = True)
            embedVar.add_field(name = '`Task`', value = "Send `{}` card to this bot".format(self.card), inline = True)
            embedVar.add_field(name = 'Status', value = "❌", inline = True)

            embedVar.add_field(name = self.bidderName, value = "➡️", inline = True)
            embedVar.add_field(name = '`Task`', value = "Send $`{}` to this Venmo".format(self.price), inline = True)
            embedVar.add_field(name = 'Status', value = "❌", inline = True)

        return embedVar
