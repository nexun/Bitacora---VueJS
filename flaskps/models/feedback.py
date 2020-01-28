from flaskps.models.model import Model


class Feedback(Model):

    @classmethod
    def data(cls, aDescription, aTitle=None, anAltRoute=None, aRouteName=None):
        '''
        Returns a dictionary with the data to be passed to the view.

        Parameters:
            aDescription: The main message to be shown.
            aTitle (optional): The title of the feedback.
            anAltRoute (optional): An alternate route to be offered.
            aRouteName (optional): The name to be shown for the altRoute.

        Returns:
            Dictionary{title, description, altRoute, routeName}
        '''

        return {
            'title': aTitle,
            'description': aDescription,
            'altRoute': anAltRoute,
            'routeName': aRouteName
        }
