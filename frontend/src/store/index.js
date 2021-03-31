import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

import user from './modules/user';
import recipe from './modules/recipe';
import ingredients from './modules/ingredients';
import header from './modules/header';
import review from './modules/review';
import hashtag from './modules/hashtag';

const store = new Vuex.Store({
  modules: {
    user,
    recipe,
    ingredients,
    header,
    review,
    hashtag,
  },
});

export default store;
