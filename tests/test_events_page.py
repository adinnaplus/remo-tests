#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from random import randrange

import pytest
from unittestzero import Assert
from selenium.webdriver.support.ui import WebDriverWait

from pages.events import Events


class TestEventsPage:

    @pytest.mark.nondestructive
    def test_events_map_is_visible(self, mozwebqa):
        events_page = Events(mozwebqa)
        events_page.go_to_events_page()
        Assert.true(events_page.is_events_map_visible)

    @pytest.mark.nondestructive
    def test_events_table_is_visible(self, mozwebqa):
        events_page = Events(mozwebqa)
        events_page.go_to_events_page()
        Assert.true(events_page.is_events_table_visible)

    @pytest.mark.nondestructive
    def test_filter_results_by_owner(self, mozwebqa):
        query = u' John Giannelos '
        events_page = Events(mozwebqa)
        events_page.go_to_events_page()
        events_page.filter_for(query)

        WebDriverWait(mozwebqa.selenium, mozwebqa.timeout).until(
            lambda s: s.find_element_by_id('canvasLoader').is_displayed())

        Assert.equal(u'John Giannelos', events_page.event_profile_owner_text)
