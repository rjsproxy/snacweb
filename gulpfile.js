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
var uglify = require('gulp-uglify');
var sourcemaps = require('gulp-sourcemaps');
var rename = require('gulp-rename');
var minify = require('gulp-minify-css');

var sass = require("gulp-sass");
//var filter = require('gulp-filter');
//var sourcemaps = require('gulp-sourcemaps');
//var shell = require('gulp-shell'); 






var config = {
    bowerPath: './bower_components',
    staticPath: './static',
    buildPath: 'dist',
}

var sassfiles = 'website/wiki/templates/wiki/base.scss';

// RJS: investigate method to "notify" via browser?

function errorHandler (error) {
    console.log(error.toString());
    this.emit('end');
}


gulp.task('bower', function() { 
    // Install Bower Packages.
    return bower().pipe(gulp.dest(config.bowerPath)); 
});


// fonts.

var fontSources = [
    config.bowerPath + '/fontawesome/fonts/**/*',
    config.bowerPath + '/bootstrap-sass/assets/fonts/**/*',
]

gulp.task('fonts', function() { 
    return gulp.src(fontSources)
        .pipe(gulp.dest(config.staticPath + '/fonts')); 
});

gulp.task('fonts-build', function() { 
    return gulp.src(fontSources)
        .pipe(gulp.dest(config.buildPath + '/fonts')); 
});

// Javascript hacks.

gulp.task('js', function() {  
    return gulp.src([
            config.bowerPath + '/jquery/dist/jquery.js',
            // config.bowerPath + '/holderjs/holder.js',
            config.bowerPath + '/bootstrap-sass/assets/javascripts/bootstrap.js'
        ])
        .pipe(concat('snac.js'))
        .pipe(uglify())
        .pipe(gulp.dest(config.staticPath));
});

gulp.task('js-build', ['js'], function() {
    return gulp.src(config.staticPath + '/snac.js')
        .pipe(gulp.dest('dist'));
});

// Convert Sass files to CSS.

gulp.task('css', function () {
    return gulp.src([
            'website/wiki/templates/wiki/base.scss',
        ])
        .pipe(sourcemaps.init())
        .pipe(sass({
            outputStyle: 'compressed',
            //outputStyle: 'nested',
            //precision: 10,
            includePaths: ['.']
        })).on('error', errorHandler)
        .pipe($.postcss([
            require('autoprefixer-core')({browsers: ['last 2 version']})
        ]))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(config.staticPath + '/wiki'))
        .pipe(reload({stream: true}));
});

gulp.task('css-build', ['css'], function () {
    return gulp.src(config.staticPath + '/wiki/base.css')
        .pipe(minify())
        //.pipe(rename({ extname: '.min.css' }))
        .pipe(gulp.dest(config.buildPath + '/wiki'))
});


        //.pipe(shell([
        //    'virtualenv/bin/python website/manage.py collectstatic --noinput'
        //]))
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

//gulp.task('bootstrap', function(){
//    return gulp.src('index.js')
//        .pipe(gulp.dest('dist'));
//});


//gulp.task('serve', function() {
//gulp.task('serve', ['sass'], function() {
gulp.task('default', ['sass'], function() {

    browserSync.init({
        notify: false,
        //proxy: '203.28.246.145:9898',
        proxy: '127.0.0.1:3002',
        //proxy: 'charlie.snac.unimelb.edu.au:3002',
        //proxy: '192.168.100.9:8000',
    });

    gulp.watch([
        'website/wiki/templates/wiki/*.scss',
        'website/wiki/templates/wiki/*.html',
        //'website/snac/static/snac/js/*.js'
    ]).on('change', reload);

    // Watch the sassfiles and run sass job on change.
    gulp.watch(sassfiles, ['sass']);

}); 




