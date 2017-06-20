/////////////////////////////////////////////////
//                                             //  
//                               __            //  
//   __    __   _____           |__|  _____    //  
//  |  |/\|  | /     \   ____   |  | /     \   //  
//  |        ||   o   | |    |  |  ||   o   |  //  
//  |___/\___| \_____/  |____|  |__| \_____/   //  
/////////////////////////////////////////////////
//  2016/03/20 by DKZ https://davidkingzyb.github.io

terminal.init();

wtf.$('#title').setAttribute('class', 'animated fadeOut');

function showTitle(title) {
    wtf.$('#title').innerHTML = title;
    wtf.$('#title').setAttribute('class', '');
}

function hideTitle() {
    wtf.$('#title').innerHTML = 'W O . I O';
    wtf.$('#title').setAttribute('class', 'hidden');
}

var alerttimer;

function showAlert(alert, hidetime) {
    wtf.$('#loading').innerHTML = alert;
    var hidetime = hidetime || 3000;
    if (alerttimer) {
        clearTimeout(alerttimer);
    }
    wtf.$('#loading').setAttribute('class', '');
    alerttimer = setTimeout(function() {
        wtf.$('#loading').setAttribute('class', 'hidden');
    }, hidetime);
}
