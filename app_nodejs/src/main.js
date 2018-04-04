// boilerplate nodejs/express app
// Copyright (c) 2018 Jozef Van den broeck, All Rights Reserved
// vim: set ts=4 sw=4 noexpandtab :
'use strict';

const express = require('express');
const app = express();

app.get('/', (req, res) => {
	res.json({ hello : 'there' });
});

app.listen(8080, '0.0.0.0');
