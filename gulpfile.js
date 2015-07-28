/*global -$ */
'use strict'

// gulp.watch : https://www.npmjs.com/package/gulp-watch
// browser sync : http://www.browsersync.io/docs/options/

var gulp = require('gulp');
var shell = require('gulp-shell')
var $ = require('gulp-load-plugins')();
var browserSync = require("browser-sync");
var reload = browserSync.reload;

//var sass = require("gulp-sass");
//var filter = require('gulp-filter');
//var sourcemaps = require('gulp-sourcemaps');
//var shell = require('gulp-shell'); 

var sassfiles = 'website/snac/sass/*.scss';

// RJS: investigate method to "notify" via browser?

function errorHandler (error) {
    console.log(error.toString());
    this.emit('end');
}

// Convert Sass files to CSS.

gulp.task('sass', function () {
    return gulp.src('website/snac/sass/snac.scss')
        .pipe($.sourcemaps.init())
        .pipe($.sass({
            outputStyle: 'nested',
            precision: 10,
            includePaths: ['.']
            //,
            //onError: console.error.bind(console, 'Sass error:')
        })).on('error', errorHandler)
        .pipe($.postcss([
            require('autoprefixer-core')({browsers: ['last 1 version']})
        ]))
        .pipe($.sourcemaps.write())
        .pipe(gulp.dest('website/snac/static/snac/css'))
        .pipe(shell([
            'virtualenv/bin/python website/manage.py collectstatic --noinput'
        ]))
        .pipe(reload({stream: true}));
});



//gulp.task('serve', function() {
//gulp.task('serve', ['sass'], function() {
gulp.task('default', ['sass'], function() {

    browserSync.init({
        notify: false,
        //proxy: '203.28.246.145:9898',
        //proxy: '127.0.0.1:8000',
        proxy: '203.28.247.201:2000',
        //proxy: '192.168.100.9:8000',
    });

    gulp.watch([
        'website/snac/static/snac/css/snac.css',
        'website/snac/templates/*/*.html'
    ]).on('change', reload);

    gulp.watch(sassfiles, ['sass']);

}); 

