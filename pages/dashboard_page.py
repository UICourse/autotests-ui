from playwright.sync_api import Page, expect

from components.charts.chart_view_component import ChartViewComponent
from components.navigation.navbar_component import NavbarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.scores_chart = ChartViewComponent(page, 'scores', 'scatter')
        self.courses_chart = ChartViewComponent(page, 'courses', 'pie')
        self.students_chart = ChartViewComponent(page, 'students', 'bar')
        self.activities_chart = ChartViewComponent(page, 'activities', 'line')

        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible_dashboard_title(self):
        expect(self.dashboard_title).to_be_visible()
        expect(self.dashboard_title).to_have_text('Dashboard')

    def check_visible_students_chart(self):
        self.students_chart.check_visible('Students')

    def check_visible_activities_chart(self):
        self.activities_chart.check_visible('Activities')

    def check_visible_courses_chart(self):
        self.courses_chart.check_visible('Courses')

    def check_visible_scores_chart(self):
        self.scores_chart.check_visible('Scores')
