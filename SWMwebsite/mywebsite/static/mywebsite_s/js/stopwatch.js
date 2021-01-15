var ms = 0;
var state = 0;

function start()
{
if (state == 0)
{
state = 1;
then = new Date();
then.setTime(then.getTime() - ms);
}
}
function stop()
{
if (state == 1)
{
state = 0;
now = new Date();
ms = now.getTime() - then.getTime();
document.stpw.time.value = ms;
}
}

function swreset()
{
state = 0;
ms = 0;
document.stpw.time.value = ms;
}

function display()
{
setTimeout("display();", 10);
if (state == 1)
{
now = new Date();
ms = now.getTime() - then.getTime();
document.stpw.time.value = ms;
}
}