#!usr/bin/node

exports.converter = fucntion (base) {
	return function (number) {
    return number.toString(base);
  };
};
