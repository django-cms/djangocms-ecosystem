from datetime import datetime
from typing import TextIO
from requests import get

url = "https://raw.githubusercontent.com/django-cms/djangocms-ecosystem/refs/heads/main/README.md"

ecosystem = []
ecosystem_timestamp = None

check = "\u2713  "
cross = "\u00d7  "


def read_ecosystem() -> list[dict[list[dict[str, str]]]]:
    """
    Reads and returns the ecosystem configuration.

    This function checks if the global variable `ecosystem` is already populated.
    If not, it reads the ecosystem configuration using the `_read_ecosystem` function
    and assigns it to the `ecosystem` variable.

    Returns:
        The ecosystem configuration.
    """
    global ecosystem, ecosystem_timestamp

    if not ecosystem or (datetime.now() - ecosystem_timestamp).days >= 1:
        ecosystem = _read_ecosystem()
        ecosystem_timestamp = datetime.now()
    return ecosystem


def _read_ecosystem() -> list[dict[list[dict[str, str]]]]:
    """
    Reads and parses ecosystem data from a markdown source.

    The function fetches markdown content from a specified URL, processes it, and organizes it into a structured format.
    The markdown content is expected to have chapters and sub-sections with specific formatting:
    - Chapters start with "## " and contain a title and description.
    - Sub-sections within chapters start with "### " and contain a title, description, and properties.
    - Properties within sub-sections are listed with "* " and are key-value pairs separated by a colon.

    Returns:
        list: A list of dictionaries representing the ecosystem structure. Each dictionary contains:
            - title (str): The title of the chapter or sub-section.
            - description (str): The description of the chapter or sub-section.
            - content (list): A list of sub-sections within a chapter, each represented as a dictionary with:
                - title (str): The title of the sub-section.
                - description (str): The description of the sub-section.
                - properties (dict): A dictionary of properties for the sub-section.
    """
    ecosystem_md = get(url).text
    ecosystem = []
    chapter = {}
    content = {}

    lines = ecosystem_md.split("\n")
    while lines:
        line = lines.pop(0)
        if line.startswith("## "):
           chapter = {"title": line[3:], "description": "", "content": []}
           content = {}
           ecosystem.append(chapter)
        elif line.startswith("### ") and chapter and "content" in chapter:
            content = {"title": line[4:], "description": "", "properties": {}}
            chapter["content"].append(content)
        elif line.startswith("* "):
            if content and "properties" in content and ":" in line:
                key, value = line[2:].split(":", 1)
                if ", " in value:
                    value = [item.strip() for item in value.split(", ")]

                else:
                    value = value.strip()
                content["properties"][key] = value
        elif line:
            if "description" in content:
                content["description"] += line + " "
            elif "description" in chapter:
                chapter["description"] += line + " "
    return ecosystem


def get_chapter(name: str) -> dict[list[dict[str, str]]]:
    """
    Retrieve a chapter from the ecosystem by its title.

    Args:
        name (str): The title of the chapter to retrieve.

    Returns:
        dict: The chapter dictionary if found, otherwise None.
    """
    ecosystem = read_ecosystem()
    return next(
        (chapter for chapter in ecosystem if chapter["title"] == name), None
    )


def sorted_versions(versions: list) -> list:
    """
    Sorts a list of version strings in descending order.

    Args:
        versions (list): A list of version strings (e.g., ["1.0.0", "2.0.0", "1.2.3"]).

    Returns:
        list: The sorted list of version strings in descending order.
    """
    def key(version: str) -> tuple:
        """
        Converts a version string into a tuple of integers for sorting.

        Args:
            version (str): The version string to convert.

        Returns:
            tuple: A tuple of integers representing the version.
        """
        try:
            return tuple(map(int, version.split(".")))
        except ValueError:
            return (999, 999, 999)  # Fallback for invalid version formats
    return sorted(versions, key=key, reverse=True)


def get_django_versions():
    """
    Retrieve a sorted list of Django versions used in the "django CMS" chapter.

    This function fetches the "django CMS" chapter content, extracts the Django
    versions specified in the content properties, and returns a sorted list of
    these versions. If the "django CMS" chapter is not found, it returns an
    empty list.

    Returns:
        list: A sorted list of Django versions used in the "django CMS" chapter.
    """
    djangocms = get_chapter("django CMS")
    if djangocms is None:
        return []
    versions = set()
    for content in djangocms["content"]:
        if "django" in content["properties"]:
            for version in content["properties"]["django"]:
                versions.add(version)
    return sorted_versions(versions)


def get_python_versions():
    """
    Retrieve a sorted list of Python versions supported by django CMS.

    This function fetches the chapter related to "django CMS" and extracts
    the Python versions mentioned in the content properties. It collects
    these versions into a set to ensure uniqueness and then returns them
    as a sorted list.

    Returns:
        list: A sorted list of unique Python versions supported by django CMS.
    """
    djangocms = get_chapter("django CMS")
    versions = set()
    if djangocms:
        for content in djangocms["content"]:
            if "python" in content["properties"]:
                for version in content["properties"]["python"]:
                    versions.add(version)
    return sorted_versions(versions)


def get_djangocms_versions():
    """
    Extracts and returns a sorted list of django CMS versions from the chapter content.

    This function retrieves the chapter content for "django CMS" and extracts the version
    numbers from the titles that start with "django CMS". The extracted versions are then
    sorted and returned as a list.

    Returns:
        list: A sorted list of django CMS version numbers.
    """
    djangocms = get_chapter("django CMS")
    versions = set()
    if djangocms:
        for content in djangocms["content"]:
            if "title" in content and content["title"].startswith("django CMS"):
                versions.add(content["title"][10:].strip())
    return sorted_versions(versions)


def get_python_support(version: str) -> list:
    """
    Retrieve the list of supported Python versions for a specific django CMS version.

    Args:
        version (str): The version of django CMS to check for Python support.

    Returns:
        list: A list of supported Python versions for the specified django CMS version.
              Returns an empty list if the version is not found or if there are no supported Python versions.
    """
    if djangocms := get_chapter("django CMS"):
        for content in djangocms["content"]:
            if content["title"] == f"django CMS {version}":
                return content["properties"].get("python", [])
    return []


def get_django_support(version: str) -> list:
    """
    Retrieve the list of supported Django versions for a specific django CMS version.

    Args:
        version (str): The version of django CMS to check for Django support.

    Returns:
        list: A list of supported Django versions for the specified django CMS version.
              Returns an empty list if the version is not found or if there are no supported Django versions.
    """
    if djangocms := get_chapter("django CMS"):
        for content in djangocms["content"]:
            if content["title"] == f"django CMS {version}":
                return content["properties"].get("django", [])
    return []


def get_LTS_support(version: str) -> str:
    """
    Retrieve the Long Term Support (LTS) information for a specified version of django CMS.

    Args:
        version (str): The version of django CMS for which to retrieve LTS information.

    Returns:
        str: A list of LTS support details for the specified version. If no LTS information is found, an empty list is returned.
    """
    djangocms = get_chapter("django CMS")
    if djangocms:
        for content in djangocms["content"]:
            if content["title"] == f"django CMS {version}":
                lts = content["properties"].get("LTS", [])
                if isinstance(lts, list):
                    return lts
                return [lts]
    return []


_english_months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}


def english_date(number_string):
    """
    Converts a date string in the format "MM/YYYY" to a more readable English format.

    Args:
        number_string (str): The date string in the format "MM/YYYY".

    Returns:
        str: The date string in the format "Month YYYY" if the month is recognized,
             otherwise returns the original input string.
    """
    try:
        month, year = number_string.split("/")
    except ValueError:
        return number_string
    if month in _english_months:
        return f"{_english_months[month]} {year}"
    return number_string


def write_LTS_table(f: TextIO):
    """
    Writes a table of Django CMS versions and their support for different Python and Django versions to the given file.

    The table includes:
    - Django CMS versions
    - Supported Python versions
    - Supported Django versions
    - LTS (Long Term Support) status for Django versions

    Args:
        f (TextIO): A file-like object to which the table will be written.

    The function retrieves the versions of Django CMS, Python, and Django, and constructs a table that shows which
    versions of Python and Django are supported by each version of Django CMS. It also indicates LTS support for
    Django versions.
    """
    djangocms = get_djangocms_versions()
    python_versions = get_python_versions()
    django_versions = get_django_versions()
    separator = "========== " + len(python_versions[:-1]) * "==== " + "==== " + len(django_versions[:-1]) * "==== " + "===="
    sep2      = "---------- " + len(python_versions[:-1]) * "-----" + "---- " + len(django_versions[:-1]) * "-----" + "----"
    print(separator, file=f)
    print(f"Django CMS {'Python':<{5 * len(python_versions)}}Django", file=f)
    print(sep2, file=f)
    print("\\          " + " ".join(f"{py:4}" for py in python_versions) + " " + "  ".join(django_versions), file=f)
    print(separator, file=f)
    for cms in djangocms:
        python_support = get_python_support(cms)
        django_support = get_django_support(cms)
        lts_support = get_LTS_support(cms)
        if any([python_support, django_support]):
            python = [f"{check if py in python_support else cross} " for py in python_versions]
            django = [('LTS' if dj in lts_support else check) if dj in django_support else cross
                    for dj in django_versions]
            print(f"{f'{cms}.x':10} " + " ".join(python) + " " + "  ".join(django), file=f)
    print(separator, file=f)


def write_current_LTS(f: TextIO, current: bool = True):
    """
    Writes the current Long-Term Support (LTS) versions of django CMS to the provided file-like object.
    The result is a rst formatted table with the following columns:
        - django CMS: The LTS version of django CMS.
        - Feature freeze: The date when the LTS version was feature frozen.
        - LTS: The LTS version of django CMS.
        - End of long-term support: The date when the LTS version will no longer be supported.

    Args:
        f (file-like object): The file-like object to write the LTS information to.
        current (bool, optional): If True, writes the LTS versions that are currently supported.
                                  If False, writes the LTS versions that are no longer supported.
                                  Defaults to True.

    The function retrieves the django CMS versions and Django timelines, then iterates through the
    django CMS versions to find those marked as LTS. For each LTS version, it retrieves the end of
    support date from the Django timelines and writes the information in a formatted table to the
    provided file-like object.
    """
    django = get_chapter("Django timelines")
    chapter = get_chapter("django CMS")
    if chapter:

        def get_end_of_support(version):
            for dj in django["content"]:
                if dj["title"] == version:
                    return dj["properties"].get("end-of-support", "unknown")
            return "unknown"

        print("========== ============== ====== ========================", file=f)
        print("django CMS Feature freeze Django End of long-term support", file=f)
        print("========== ============== ====== ========================", file=f)

        this_year = datetime.now().strftime("%Y")
        this_month = datetime.now().strftime("%m")
        for cms in chapter["content"]:
            if cms["title"].startswith("django CMS ") and "LTS" in cms["properties"]:
                lts_versions = cms["properties"].get("LTS", [])
                if not isinstance(lts_versions, list):
                    lts_versions = [lts_versions]
                for lts in lts_versions:
                    end_of_support = get_end_of_support(lts)
                    try:
                        month, year = end_of_support.split("/")
                    except ValueError:
                        month, year = "12", "2099"
                    if (year == this_year and month >= this_month or year > this_year) is current:
                        print(f"{cms['title'][11:] + '.x':10} "
                            f"{english_date(cms['properties'].get('feature-freeze', '-')):<14} "
                            f"{lts:<6} {english_date(end_of_support)}", file=f)
        print("========== ============== ====== ========================", file=f)


def split_description(description: str, max_length: int = 60) -> list[str]:
    """
    Splits words of a description string into a list of strings, each with a maximum length.

    Args:
        description (str): The input string to be split.
        max_length (int, optional): The maximum length of each split string. Defaults to 60.

    Returns:
        list[str]: A list of strings, each with a length up to max_length.
    """
    words = description.split()
    lines = []
    current_line = []

    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= max_length:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]

    if current_line:
        lines.append(" ".join(current_line))

    return lines


def write_plugin_table(f: TextIO, chapter: str = "CMS packages", deprecated=False):
    """
    Writes a table (rst formatted) of CMS packages to the given file-like object.

    Args:
        f (file-like object): The file-like object to write the table to.
        chapter (str, optional): The chapter name to retrieve plugins from. Defaults to "CMS packages".
        deprecated (bool, optional): If True, only include deprecated plugins. If False, only include non-deprecated plugins. Defaults to False.

    The table includes the following columns:
        - Package: The title of the plugin.
        - Description: A brief description of the plugin.
        - Status: The status or grade of the plugin.
        - Supported Versions: The versions of Django CMS that the plugin supports.

    The table is formatted with headers and separators for readability.
    """
    chapter = get_chapter(chapter)

    if chapter:
        print("============================== ============================================================ =========== ==================", file=f)
        print("Package                        Description                                                  Status      Supported Versions", file=f)
        print("============================== ============================================================ =========== ==================", file=f)
        for plugin in chapter["content"]:
            if bool(plugin["properties"].get("deprecated", False)) is deprecated:
                status = plugin["properties"].get("grade", "unknown")
                versions = plugin["properties"].get("django CMS", [])
                if not isinstance(versions, list):
                    versions = [versions]
                versions = ", ".join(versions)
                description = plugin['description']
                lines = split_description(description)
                print(f"{plugin['title']:<30} {lines[0]:<60} {status:<13} {versions}", file=f)
                for line in lines[1:]:
                    print(f"{'':30} {line:<60}", file=f)
        print("========================== ============================================================ =========== ==================", file=f)
