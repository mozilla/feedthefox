App = Ember.Application.create();

App.Router.map(function() {
    this.resource('about', {path: '/'});
    this.resource('about');
    this.resource('news');
    this.resource('dashboard');
});
