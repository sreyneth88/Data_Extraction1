var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

var args = process.argv.slice(2);
var link=args[0];
console.log(link);
var website="https://www.instagram.com/"+link;
request(website, function (error, response, html) {
	if (!error && response.statusCode == 200) {
		var data=html.toString();
		var debut=data.indexOf("sharedData")+13;
	    var fin=data.indexOf(";<");
	    var chaine=data.substring(debut,fin);
	    var jsonObj = JSON.parse(chaine);
	    var counter=jsonObj.entry_data.ProfilePage[0].user.media;
	    if(counter.hasOwnProperty("nodes")){
	    	var i=0;
		    for(i=0;i<jsonObj.entry_data.ProfilePage[0].user.media.nodes.length;i++){
		    	var link='https://www.instagram.com/p/'+jsonObj.entry_data.ProfilePage[0].user.media.nodes[i].code;
		    	console.log(link);
		    	fs.appendFile("safirFollower.csv",link+"\n", encoding='utf8', function (err) {
	              if (err) throw err;
	           	});
		    	/*
			    	var timepro=jsonObj.entry_data.ProfilePage[0].user.media.nodes[i].date;
			    	var currenttime = (new Date).getTime()/1000;
			    	console.log("currenttime "+currenttime);
			        var different =currenttime -timepro;
			        if (different <= 172800){
			           fs.appendFile("safirFollower.csv",link+"\n", encoding='utf8', function (err) {
			              if (err) throw err;
			           });
			        }else{
			          console.log("more than 2 day");
			        }
			    */
		    }
	    }else{
	    	console.log("No Property ");
	    }   

	}else{
		console.log("error "+response.statusCode);

	}
});
