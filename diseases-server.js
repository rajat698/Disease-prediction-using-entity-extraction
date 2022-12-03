const fs = require('fs');
const http = require('http');

var path_to_project = 'C:\\Users\\biega\\Disease-prediction-using-entity-extraction';
var path_to_jena = 'C:\\Users\\biega\\apache-jena-4.6.1\\lib';
var option;
var update = false;

http.createServer((request, response) => {
    if (request.method === 'GET' && (request.url === '/' || request.url === '/?')) {
        fs.readFile('index.html', function (error, index) {
            if (error) {
                response.writeHead(404);
                response.write('Content you are looking for not found! :(');
            } else {
                response.writeHead(200, { 'Content-Type': 'text/html' });
                response.write(index);
            }
            response.end();
        });
    } else if (request.method === 'POST' && request.url === '/query') {
        update = false;
        let body = [];
        request.on('data', (chunk) => {
          body.push(chunk);
        }).on('end', () => {
            body = Buffer.concat(body).toString();
            let formData = body.split('&');
            // Write the CMD script
            option = formData[1].split('=')[1].toLowerCase();
            let criteria = formData[0].split('=')[1];
            criteria = criteria.replace(/\+/g, " ");
            console.log("option = " + option);
            console.log("criteria = " + criteria);
            let script = writeScript();
            fs.writeFile('criteria.txt', criteria, function (err) {
                fs.writeFile('diseases.cmd', script, function (err) {
                    // Invoke SPARQL program
                    var exec = require('child_process').exec;
                    exec('start diseases.cmd', function (error, stdout, stderr) {
                        if (error !== null) {
                            console.log("exec error: " + error);
                        } else {
                            // Read the result from the output file
                            fs.readFile('result.txt', 'utf-8', function (err, data) {
                                if (err != null) console.log("Error reading output.txt!");
                                else {
                                    response.writeHead(200, { 'Content-Type': 'text/html' });
                                    let result = '<!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml"><head><meta charset="utf-8" />'
                                    + '<title>Diseases Database and Entity Extraction</title><body style="background-color:lightskyblue"><div style="text-align:center">'
                                    + '<h2>Results</h2><form action="/" method="get">'
                                    + data + '<br>'
                                    + '<div div style="padding-top:10px"><input type="submit" value="Back" /></div></form></div></body></html>'
                                    response.write(result);
                                }
                                response.end();
                            });
                        }   
                    });
                });
            });
        });
    } else if (request.method === 'POST' && request.url === '/update') {
        update = true;
        let body = [];
        request.on('data', (chunk) => {
          body.push(chunk);
        }).on('end', () => {
            body = Buffer.concat(body).toString();
            body = body.substring(5);
            body = body.replace(/\+/g, " ");
            body = body.replace(/%3A/g, ":");
            body = body.replace(/%3C/g, "<");
            body = body.replace(/%2F/g, "/");
            body = body.replace(/%23/g, "#");
            body = body.replace(/%3E/g, ">");
            body = body.replace(/%0D/g, "\r");
            body = body.replace(/%0A/g, "\n");
            body = body.replace(/%7B/g, "{");
            body = body.replace(/%7D/g, "}");  
            body = body.replace(/%3F/g, "?");
            body = body.replace(/%3D/g, "=");
            body = body.replace(/%09/g, "\t");
            body = body.replace(/%27/g, "\'");
            body = body.replace(/%28/g, "(");
            body = body.replace(/%29/g, ")");
            body = body.replace(/%2C/g, ",");
            body = body.replace(/%22/g, "\""); 
            body = body.replace(/%E2/g, "—");
            body = body.replace(/%80/g, "");
            body = body.replace(/%94/g, "");
            console.log("text = " + body);
            
            // Write the CMD script
            option = 'update';
            updateCommands = '';
            let script = writeScript();
            fs.writeFile('diseases.cmd', script, function (err) {
                // Invoke SPARQL program
                fs.writeFile('text.txt', body, function (err) {
                    var exec = require('child_process').exec;
                    exec('start diseases.cmd', function (error, stdout, stderr) {
                        fs.readFile('index.html', function (error, index) {
                            if (error) {
                                console.log('Content you are looking for not found! :(');
                            } else {
                                console.log("Database updated!");
                            }
                        });

                    });
                    response.writeHead(200, { 'Content-Type': 'text/html' });
                    let result = '<!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml"><head><meta charset="utf-8" />'
                        + '<title>Diseases Database and Entity Extraction</title><body style="background-color:lightskyblue"><div style="text-align:center">'
                        + '<h2>Updating database. Check back later!</h2><form action="/" method="get">'
                        + '<div div style="padding-top:10px"><input type="submit" value="Back" /></div></form></div></body></html>'
                    response.write(result);
                    response.end();
                });
            });
        });
      }
}).listen(8080, function() {
    console.log('diseases-server listening on port 8080...');
});

function writeScript() {
    let script = 'cd ' + path_to_project + '\n';
    if (update) {
        script += 'python app.py\n';
        script += 'javac PrepareDataInsert.java\n';
        script += 'java PrepareDataInsert\n';
    }
    script += 'javac -cp ".;' + path_to_jena + '\\*" MedicalConditions.java\n'
    + 'java -cp ".;' + path_to_jena + '\\*"'
    + ' MedicalConditions ' + option + '\n' 
    + 'exit'
    return script;
}