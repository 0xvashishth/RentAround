let auth_token;
$('#country').click(function() {
    getCountries();
    $('#country').unbind('click');
})

$(document).ready(function() {
    $.ajax({
        type: 'get',
        url: 'https://www.universal-tutorial.com/api/getaccesstoken',
        success: function(data) {
            auth_token = data.auth_token;
        },
        error: function(error) {
            console.log(error);
        },
        headers: {
            "Accept": "application/json",
            "api-token": "VzUm_xhJS2hSyYryVSNvh8FfqH_ZdIRW83oQ1Ib_Z9Q17HuVx0oh8k23TY37P3bWGG8",
            "user-email": "vasutemporarylc@gmail.com"
        }
    })
})

function getCountries() {
    $.ajax({
        type: 'get',
        url: 'https://www.universal-tutorial.com/api/countries',
        success: function(data) {
            $('#country').empty();
            data.forEach((ele) => {
                $('#country').append(`<option value="${ele.country_name}">${ele.country_name}</option>`);
            })
            getStates();
        },
        error: function(error) {
            console.log(error);
        },
        headers: {
            "Authorization": "Bearer " + auth_token,
            "Accept": "application/json"
        }
    })
}

function getStates() {
    $.ajax({
        type: 'get',
        url: 'https://www.universal-tutorial.com/api/states/' + $('#country').val(),
        success: function(data) {
            $('#state').empty();
            data.forEach((ele) => {
                $('#state').append(`<option value="${ele.state_name}">${ele.state_name}</option>`);
            })
            getCities();
        },
        error: function(error) {
            console.log(error);
        },
        headers: {
            "Authorization": "Bearer " + auth_token,
            "Accept": "application/json"
        }
    })
}

function getCities() {
    $.ajax({
        type: 'get',
        url: 'https://www.universal-tutorial.com/api/cities/' + $('#state').val(),
        success: function(data) {
            $('#city').empty();
            data.forEach((ele) => {
                $('#city').append(`<option value="${ele.city_name}">${ele.city_name}</option>`);
            })
        },
        error: function(error) {
            console.log(error);
        },
        headers: {
            "Authorization": "Bearer " + auth_token,
            "Accept": "application/json"
        }
    })
}