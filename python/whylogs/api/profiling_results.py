from whylogs.core import DatasetProfile, DatasetProfileView


class ProfilingResults:
    """
    A holder object for profiling results.

    A whylogs.log call can result in more than one profile. This wrapper class
    simplifies the navigation among these profiles.

    Note that currently we only hold one profile but we're planning to add other
    kinds of profiles such as segmented profiles here.
    """

    def __init__(self, profile: DatasetProfile):
        self._profile = profile

    def get_profile(self) -> DatasetProfile:
        return self._profile

    def view(self) -> DatasetProfileView:
        return self._profile.view()
