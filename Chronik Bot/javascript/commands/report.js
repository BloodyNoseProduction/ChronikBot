const Discord = require("discord.js")
module.exports.run = async (bot, message, args) => {

    let rUser = message.guild.member(message.mentions.users.first() || message.guild.member.get([0]));
    if(!rUser) return message.channel.send("User not found!");
    let reason = args.join(" ").slice(22);

    let reportEmbed = new Discord.RichEmbed()
    .setDescription("Reports")
    .setColor("#15f153")
    .addField("Reported User", `${rUser} with ID: ${rUser.id}`)
    .addField("Reporting by", `${message.author} with ID: ${message.author.id}`)
    .addField("Channel", message.channel)
    .addField("Time", message.createdAt)
    .addField("Reason", reason);

    let reportschannel = message.guild.channels.find(`name`,"reports");
    if(!reportschannel) return message.channel.send("Channel: reports not found");
    message.delete().catch(O_o=>{}); //catch and delete
    reportschannel.send(reportEmbed);
}

module.exports.help = {
    name: "report"
}