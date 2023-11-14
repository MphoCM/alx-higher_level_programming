#!/usr/bin/node
let counter = 0

export.logMe = function (item) {
	console.log(`${counter++}: ${item}`);
};
