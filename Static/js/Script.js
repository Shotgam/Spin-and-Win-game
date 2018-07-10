$('document').ready(function () {
    $("#Spin_And_Win_Btn").click(function () {
        $('#Prize_Text_Field').text('Redeem Your Prize In App.');
        $('.Prize_Box_One').css('background-color','gray');
        $('#Attempt_One').css('background-color','#ff9b9b');
        $('#Attempts_Remaining').text('0 Attempts Left');
        $('#Spin_And_Win_Btn').text('No More Spin & Win');
        $('#Spin_And_Win_Btn').css('background-color','gray');
        SpinTheWheel(180);
    });
    function SpinTheWheel(degree) { 
        $('#Spin_The_Wheel img').css('transform','rotate(180deg)');
    }  
});



