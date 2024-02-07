// ==UserScript==
// @name         GitHub Actions Filter Button
// @namespace    http://www.nxw.name
// @version      2024-02-06
// @description  Filter GitHub Actions which is not passed and quired
// @author       Xuewei Niu
// @match        https://github.com/kata-containers/kata-containers/pull/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=github.com
// @grant        none
// ==/UserScript==

var hidden = false;
var loaded = false;

function filterButtonOnClick() {
    hidden = !hidden;
    var checks = document.querySelectorAll('#partial-pull-merging div.merge-status-list.hide-closed-list.js-updatable-content-preserve-scroll-position > div');
    checks.forEach(function(check) {
        if (hidden) {
            var statusElement = check.querySelector('div:nth-child(3)');
            if (!statusElement) {
                // console.log(check, 'check status not found');
                return;
            }
            var detailsElement = check.querySelector('div:nth-child(4)');
            if (!detailsElement) {
                return;
            }

            var successful = statusElement.textContent.includes('Successful in') || statusElement.textContent.includes('Build finished');
            var required = detailsElement.textContent.includes('Required');

            if (successful || !required) {
                check.classList.add('hidden-check');
            }
        } else {
            check.classList.remove('hidden-check');
        }
    });
}

function insertFilter() {
    var hideAllChecks = document.querySelector('#partial-pull-merging div.branch-action-item.js-details-container.Details.open button');
    if (!hideAllChecks) {
        console.log('Failed to find filter button container');
        return;
    }

    loaded = true;

    var filterButton = document.createElement('button');
    filterButton.type = 'button';
    filterButton.textContent = 'Filter Not Passed and Required Checks';
    filterButton.addEventListener('click', filterButtonOnClick);

    hideAllChecks.parentNode.insertBefore(filterButton, filterButton.nextSibling);
}

function insertHiddenCheckCssStyle() {
    var styleElement = document.createElement('style');
    styleElement.type = 'text/css';
    var cssRule = document.createTextNode('.hidden-check { display: none !important }');
    styleElement.appendChild(cssRule);
    document.head.appendChild(styleElement);
}

function loopWithDelay() {
    var count = 0;

    function iterate() {
        if (loaded) {
            return;
        }
        // retry 60 times (1 min)
        if (count == 60) {
            return;
        }
        console.log("Iteration: " + count);
        count++;
        insertFilter();
        setTimeout(iterate, 1000);
    }

    iterate();
}

(function() {
    'use strict';

    var stateElem = document.querySelector('#partial-discussion-header .State');
    if (stateElem) {
        if (stateElem.getAttribute('title') !== 'Status: Open') {
            console.log('GitHub Actions Filter Button: Exit due to the status of PR is not "open".');
            return;
        }
    } else {
        console.log('GitHub Actions Filter Button: Can\'t determine PR\'s status.');
        return;
    }

    insertHiddenCheckCssStyle();

    loopWithDelay();
})();
