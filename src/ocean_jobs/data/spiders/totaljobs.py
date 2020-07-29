import scrapy
from bs4 import BeautifulSoup
import html


class JobSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["www.cwjobs.co.uk", "www.totaljobs.com"]
    start_urls = []
    NUM_PAGES = 5

    def start_requests(self):
        urls = [
            "https://www.cwjobs.co.uk/jobs/data-scientist/in-london?radius=10&s=header",
            "https://www.totaljobs.com/jobs/data-scientist/in-london?radius=10",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse1)

    def parse1(self, response):
        page_num = response.css(
            ".results-footer-links-container nav span.active::text"
        ).get()
        next_page = (
            response.url.split("?")[0]
            + response.css(
                ".results-footer-links-container nav a.btn.btn-default.next::attr(href)"
            ).extract()[0]
        )

        if int(page_num) <= 5:

            for job in response.css("div.job-title"):
                yield scrapy.Request(
                    url=str(job.css("a::attr(href)").get()), callback=self.parse2
                )

            yield scrapy.Request(url=next_page, callback=self.parse1)

    def parse2(self, response):

        company = response.css(
            "section.job-summary li[class='company icon'] div a::text"
        ).get()

        description = BeautifulSoup(
            "".join(response.css("div.job-description p").getall()), "html.parser"
        )

        salary_details = response.css(
            "section.job-summary li[class='salary icon'] div::text"
        ).get()

        job_type = response.css(
            "section.job-summary li[class='job-type icon'] div::text"
        ).get()

        yield {
            "URL": response.url,
            "Company-Recruiter": company,
            "Description": description.get_text(),
            "Salary": salary_details,
            "Job_Type": job_type,
        }
