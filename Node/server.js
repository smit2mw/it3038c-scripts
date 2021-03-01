var fs = require("fs");
var http = require("http"); 
var os = require("os");
var ip = require("ip");

var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        TotalMemBytes = os.totalmem();
        FreeMemBytes = os.freemem();
        function formatTime(seconds){  //https://stackoverflow.com/questions/28705009/how-do-i-get-the-server-uptime-in-node-js/28706630
            function pad(s){
              return (s < 10 ? '0' : '') + s;
            }
            var days = Math.floor(seconds / (60*60*24));
            var hours = Math.floor(seconds / (60*60));
            var minutes = Math.floor(seconds % (60*60) / 60);
            var seconds = Math.floor(seconds % 60);
          
            return pad(days) + ':' + pad(hours) + ':' + pad(minutes) + ':' + pad(seconds);
          }
          
          var uptime = process.uptime();
          console.log(formatTime(uptime));

        function formatBytes(bytes){
            myMem = (bytes / 1048576);
            return myMem;
        }
        
          html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${formatTime(uptime)} </p>
            <p>Total Memory: ${formatBytes(TotalMemBytes)} MB</p>
            <p>Free Memory: ${formatBytes(FreeMemBytes)} MB</p>
            <p>Number of CPUs: ${((os.cpus().length) / 2 )} </p>  
        </body>
        </html>
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");