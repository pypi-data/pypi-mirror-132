jQuery(function($) {
    'use strict';

    var $random_ads_top = $('#id_random_ads_top');
    var $random_ads_right = $('#id_random_ads_right');
    var $random_ads_left = $('#id_random_ads_left');
    var $random_ads_content = $('#id_random_ads_content');
    var $random_ads_bottom = $('#id_random_ads_bottom');

    function toggleCheckboxTop() {
        $('#id_top_banner').prop('disabled', $random_ads_top.prop('checked'));

    }
    function toggleCheckboxRight() {
        $('#id_sidebar_right_banner').prop('disabled', $random_ads_right.prop('checked'));
    }
    function toggleCheckboxLeft() {
        $('#id_sidebar_left_banner').prop('disabled', $random_ads_left.prop('checked'));
    }
    function toggleCheckboxContent() {
        $('#id_content_banner').prop('disabled', $random_ads_content.prop('checked'));
    }
    function toggleCheckboxBottom() {
        $('#id_bottom_banner').prop('disabled', $random_ads_bottom.prop('checked'));
    }
    $random_ads_top.on('change', toggleCheckboxTop);
    toggleCheckboxTop();
    $random_ads_right.on('change', toggleCheckboxRight);
    toggleCheckboxRight();
    $random_ads_left.on('change', toggleCheckboxLeft);
    toggleCheckboxLeft();
    $random_ads_content.on('change', toggleCheckboxContent);
    toggleCheckboxContent();
    $random_ads_bottom.on('change', toggleCheckboxBottom);
    toggleCheckboxBottom();
});