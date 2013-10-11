from copy import deepcopy


class facet_wrap(object):
    def __init__(self, x=None):
        self.x = x

    def __radd__(self, gg):

        x = gg.data.get(self.x)
        if x is None:
            n_wide = 1
        else:
            n_wide = x.nunique()
            gg.n_dim_x = x.nunique()

        
        if len(x)==1:
            n_high = 1
        else:
            n_high = 1
            n_high = n_wide - (n_wide / 2)
            n_wide = n_wide / 2

        gg.n_wide, gg.n_high = n_wide, n_high
        facets = []
        facets.append(self.x)
        gg.facets = facets
        gg.facet_type = "wrap"

        return deepcopy(gg)
