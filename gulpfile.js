/*global -$ */
'use strict'

// gulp.watch : https://www.npmjs.com/package/gulp-watch
// browser sync : http://www.browsersync.io/docs/options/

var gulp = require('gulp');
var shell = require('gulp-shell')
var $ = require('gulp-load-plugins')();
var browserSync = require("browser-sync");
var reload = browserSync.reload;
var bower = require('gulp-bower');
var concat = require('gulp-concat');

//var sass = require("gulp-sass");
//var filter = require('gulp-filter');
//var sourcemaps = require('gulp-sourcemaps');
//var shell = require('gulp-shell'); 

var config = {
    bowerPath: './bower_components',
    staticPath: './static'
}

var sassfiles = 'website/snac/sass/*.scss';

// RJS: investigate method to "notify" via browser?

function errorHandler (error) {
    console.log(error.toString());
    this.emit('end');
}

// Install Bower Packages.

gulp.task('bower', function() { 
    return bower()
        .pipe(gulp.dest(config.bowerPath)); 
});

// Fonts.

gulp.task('fonts', function() { 
    return gulp.src([
            config.bowerPath + '/fontawesome/fonts/**/*',
            config.bowerPath + '/bootstrap-sass/assets/fonts/**/*',
        ])
        .pipe(gulp.dest(config.staticPath + '/fonts')); 
});

// Javascript.

gulp.task('js', function() {  
    return gulp.src([
            config.bowerPath + '/jquery/dist/jquery.js',
            config.bowerPath + '/bootstrap-sass/assets/javascripts/bootstrap.js'
        ])
        .pipe(concat('snac.js'))
        .pipe(gulp.dest(config.staticPath + '/js'))
});

// Convert Sass files to CSS.

gulp.task('sass', function () {
    return gulp.src('website/snac/sass/snacweb.scss')
        .pipe($.sourcemaps.init())
        .pipe($.sass({
            outputStyle: 'nested',
            precision: 10,
            includePaths: ['.']
            //,
            //onError: console.error.bind(console, 'Sass error:')
        })).on('error', errorHandler)
        .pipe($.postcss([
            require('autoprefixer-core')({browsers: ['last 2 version']})
        ]))
        .pipe($.sourcemaps.write())
        .pipe(gulp.dest(config.staticPath + '/css'))
        //.pipe(shell([
        //    'virtualenv/bin/python website/manage.py collectstatic --noinput'
        //]))
        .pipe(reload({stream: true}));
});


/* alternative style suggested by autoprefixer
gulp.task('autoprefixer', function () {
    var postcss      = require('gulp-postcss');
    var sourcemaps   = require('gulp-sourcemaps');
    var autoprefixer = require('autoprefixer-core');

    return gulp.src('./src/*.css')
        .pipe(sourcemaps.init())
        .pipe(postcss([ autoprefixer({ browsers: ['last 2 versions'] }) ]))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('./dest'));
});
*/

gulp.task('bootstrap', function(){
    return gulp.src('index.js')
        .pipe(gulp.dest('dist'));
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
        'website/snac/templates/*/*.html',
        'website/snac/static/snac/js/*.js'
    ]).on('change', reload);

    // Watch the sassfiles and run sass job on change.
    gulp.watch(sassfiles, ['sass']);

}); 




