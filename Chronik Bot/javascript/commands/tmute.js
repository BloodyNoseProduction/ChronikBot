const Discord = require("discord.js")
const ms = require("ms")
module.exports.run = async (bot, message, args) => {
    //!!tmute @user 1s/m/h/d

    let timeout = message.guild.member(message.mentions.users.first() || message.guild.members.get(args[0]));
    if(!tmute) return message.reply("User not found.");

    if(tmute.hasPermission("MANAGE_MESSAGES")) return message.reply("User can not be muted");

    let muterole = message.guild.roles.find(`name`, "muted");

    //create roll
    if(!muterole){
        try{
            muterule = await message.guild.createRole({
                name: "muted",
                color: "#000000",
                permissions:[]
            })
            message.guild.channels.forEach(async (channel, id) => {
                await channel.overwritePermissions(muterole, {
                    SEND_MESSAGES: false,
                    ADD_REACTIONS: false
                });
            });

        }catch(e){
            console.log(e.stack);
        }
    } //end of

    let mutetime = args[1];
    if(!mutetime) return  message.reply("No mute time found fool");
    await(tmute.addRole(muterole.id));
    message.reply(`<@${tmute.id}> has been muted for ${ms(ms(mutetime))}`);

    setTimeout(function(){
        tmute.removeRole(muterole.id);
        message.channel.send(`<@${tmute.id}> has been unmuted`);
    }, ms(mutetime));

}

module.exports.help = {
    name: "Temp mute"
} 