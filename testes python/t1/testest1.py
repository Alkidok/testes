'''
const Discord = require('discord.js');
const cheerio = require('cheerio');
const request = require('request');

const bot = new Discord.Client();
const token = 'SEU_TOKEN_AQUI';

bot.on('ready', () => {
  console.log(`Logged in as ${bot.user.tag}!`);
});

bot.on('message', msg => {
  if (msg.content === '!precojogo') {
    request('https://www.siteexemplo.com.br/jogo', (error, response, html) => {
      if (!error && response.statusCode == 200) {
        const $ = cheerio.load(html);
        const preco = $('span.preco-jogo').text();
        const titulo = $('h1.titulo-jogo').text();
        const descricao = $('div.descricao-jogo').text();
        const dataLancamento = $('div.data-lancamento').text();
        const avaliacao = $('div.avaliacao-jogo').text();

        const embed = new Discord.MessageEmbed()
          .setColor('#0099ff')
          .setTitle(titulo)
          .setDescription(descricao)
          .addFields(
            { name: 'Preço', value: preco },
            { name: 'Data de lançamento', value: dataLancamento },
            { name: 'Avaliação', value: avaliacao }
          );

        msg.channel.send(embed);
      }
    });
  }
});

bot.login(token);

'''