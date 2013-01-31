var ROWS=400;

function drawPoints() {
    // Get the canvas element and its drawing context
    var canvas = document.getElementById('diagonal');
    var context = canvas.getContext('2d');
    var img = context.getImageData(0, 0, canvas.width, canvas.height);
    console.log("img.width="+img.width);
    for (k = 0; k < ROWS; k++) {
	for (r = 0; r <= k; r++) {
	    var c, x, y;
	    if (isFactor(k, r, 7)) {
		c = "green";
	    } else {
		c = "red";
	    }
	    x = getX(r);
	    y = getY(k);
	    setPixel(img, x, y, getColor(c));
	}
    }
    context.putImageData(img,0,0);
}

function setPixel(img, x, y, color) {
    i = getPixelPos(x, y, img.width);
    img.data[i] = color[0];
    img.data[i+1] = color[1];
    img.data[i+2] = color[2];
    img.data[i+3] = 255;
}

function getPixelPos(x, y, w) {
    x0 = ROWS;
    x1 = x0-y+2*x
    return 4*(y*w + x1);
}

function getX(x) {
    return x;
}

function getY(y) {
    return y;
}

function getColor(spec) {
    if (spec == "green") return [0, 255, 0];
    if (spec == "red") return [255, 0, 0];
    throw new Error("unknown color!");
}

function isFactor(k, r, a) {
    if (k < r) throw new Error("k>=r must be true!");

    k7 = toBase(k, a);
    r7 = toBase(r, a);
    for (i = 0; i < r7.length; i ++) {
	if (r7[i] > k7[i])
	    return true;
    }

    return false;
}

function toBase(i, b) {
    var arr = new Array();
    var d;
    do {
	d = i % b;
	arr.push(d);
	i = parseInt(i/b);
    } while (i > 0);
    return arr;
}
