document.addEventListener('DOMContentLoaded', function () {
    // These pieces of code were taken from the materialize website
    // They help make the pieces of content work as they should

    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav, { edge: 'right' });

    var modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);

    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd/mm/yyyy",
        i18n: { done: "Select" }
    });

    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);
});