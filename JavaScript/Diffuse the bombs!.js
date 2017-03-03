// Diffuse all of the Bombs!
/*** Bomb no.1 ***/
Bomb.diffuse(Bomb.key);

/*** Bomb no.2 ***/
Bomb.diffuse('just keep trying');
Bomb.diffuse('just keep trying');
Bomb.diffuse('just keep trying');
Bomb.diffuse('just keep trying');
Bomb.diffuse('just keep trying');


/*** Bomb no.3 ***/
Bomb.diffuse(BombKey);

/*** Bomb no.4 ***/
var diffuseTheBomb = function () {
    return true;
}
Bomb.diffuse();

/*** Bomb no.5 ***/
Bomb.diffuse(3.14159);

/*** Bomb no.6 ***/
var date = new Date();
date.setFullYear(date.getFullYear() - 4);
Bomb.diffuse(date);

/*** Bomb no.7 ***/
var code = {};
Object.defineProperty(code, "key", {
    value: 43
});
Bomb.diffuse(code);

/*** Bomb no.8 ***/
function flip(n) {
    this.num = n;
}

flip.prototype.valueOf = function () {
    this.num *= -1;
    return this.num;
}

Bomb.diffuse(new flip(11));

/*** Bomb no.9 ***/
var count = 0;
Math.random = function () {
    return (++count < 3) ? 1 : 0.5;
}
Bomb.diffuse(42)

/*** Bomb no.10 ***/
Array.prototype.valueOf = function () {
    return this.reduce(function (acc, val) {
        return acc + val;
    }, 0);
}
Bomb.diffuse("eWVz");