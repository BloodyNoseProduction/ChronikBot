const Discord = require("discord.js")
module.exports.run = async (bot, message, args) => {
    let bUser = message.guild.member(message.mentions.users.first() || message.guild.member.get([0]));
    if(!bUser) message.channel.send("User not found");
    let bReason = args.join(" ").slice(22);
    if(!message.member.hasPermission("MANAGE_MEMBERS")) return message.channel.send("You do not have Permissions to Kick this member");
    if(kUser.hasPermission("MANAGE_MEMBERS")) return message.channel,send("User can not be kicked");

    let banembed = new Discord.RichEmbed()
    .setDescription("~Ban~")
    .setColor("#ff0019")
    .addField("Banned User", `${bUser} wish ID ${bUser.id}`)
    .addField("Banned By", `<@${message.author.id}> with ID ${message.author.id}`)
    .addField("Banned In", message.channel)
    .addField("Time", message.createdAt)
    .addField("Reason", bReason);

    let banchannel = message.guild.channels.find(`name`, "reports");
    if(!banchannel) return message.channel.send("Reports channel not found");

    message.guild.member(bUser),ban(bReason);
    banchannel.send(banembed);
}

module.exports.help = {
    name: "report"
}