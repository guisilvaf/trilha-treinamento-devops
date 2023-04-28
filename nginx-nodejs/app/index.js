const express = require('express');
const app = express();

app.get('/', function(req, res){
    res.json({
        version : "1.0.0",
        description : "Container Nginx e NodeJS",
        maintaner : "Guilherme Silva <https://github.com/guisilvaf>",
    });
});

const port = process.env.PORT || 3000;

app.listen(port, function() {
    console.log("Aplicação rodando na porta: $(port)");
});