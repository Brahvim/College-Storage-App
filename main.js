import express from "express"
import bodyParser from "body-parser";

const s_app = express();

s_app.use(bodyParser.urlencoded({ extended: true }));

s_app.get("/", (p_request, p_response) => {

	p_response
		.status(200)
		.send("Hello! :D");

});

s_app.listen(8080);
