const Discord = require("discord.js")
module.exports.run = async (bot, message, args) => {
    let kUser = message.guild.member(message.mentions.users.first() || message.guild.member.get([0]));
    if(!kUser) message.channel.send("User not found");
    let kReason = args.join(" ").slice(22);
    if(!message.member.hasPermission("KICK_MEMBERS")) return message.channel.send("You do not have Permissions to Kick this member");
    if(kUser.hasPermission("KICK_MEMBERS")) return message.channel,send("User can not be kicked");

    let kickembed = new Discord.RichEmbed()
    .setDescription("~Kick~")
    .setColor("#f4e542")
    .addField("Kicked User", `${kUser} wish ID ${kUser.id}`)
    .addField("Kicked By", `<@${message.author.id}> with ID ${message.author.id}`)
    .addField("Kicked In", message.channel)
    .addField("Time", message.createdAt)
    .addField("Reason", kReason);

    let kickchannel = message.guild.channels.find(`name`, "reports");
    if(!kickchannel) return message.channel.send("Reports channel not found");


    message.guild.member(kUser).kick(kReason);
    kickchannel.send(kickembed);
}
module.exports.help = {
    name: "report"
}