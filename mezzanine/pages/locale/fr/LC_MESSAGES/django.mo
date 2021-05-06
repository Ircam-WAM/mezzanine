��          �      \      �     �  �   �  �  �     +  J   /     z     �    �  3   �     �     �     �     �     �     �                     .  �  A  L  �  �   <
  �  �
     �  [   �     T     a  h  i  C   �          5     :     @     [     `     f     z     �  &   �        	      
                                                                                     A sequence of IDs from the ``PAGE_MENU_TEMPLATES`` setting that defines the default menu templates selected when creating new pages. By default all menu templates are selected. Set this setting to an empty sequence to have no templates selected by default. A sequence of ``Page`` subclasses in the format ``app_label.model_name``, that controls the ordering of items in the select drop-down for adding new pages within the admin page tree interface. A sequence of templates used by the ``page_menu`` template tag. Each item in the sequence is a three item sequence, containing a unique ID for the template, a label for the template, and the template path. These templates are then available for selection when editing which menus a page should appear in. Note that if a menu template is used that doesn't appear in this setting, all pages will appear in it. Add An error occured with the following class. Does it subclass Page directly? Footer Home If ``True``, pages with ``login_required`` checked will still be listed in menus and search results, for unauthenticated users. Regardless of this setting, when an unauthenticated user accesses a page with ``login_required`` checked, they'll be redirected to the login page. If checked, only logged in users can view this page Left-hand tree Link Links Login required Page Pages Rich text page Rich text pages Show in menus Top navigation bar Project-Id-Version: Mezzanine
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2021-05-05 12:00+0000
PO-Revision-Date: 2013-11-09 20:02+0000
Last-Translator: Sebastián Ramírez Magrí <sebasmagri@gmail.com>
Language-Team: French (http://www.transifex.com/projects/p/mezzanine/language/fr/)
Language: fr
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n > 1);
 Une séquence d'IDs correspondant au paramètre ``PAGE_MENU_TEMPLATES`` qui définissent le menu des templates par défaut à utiliser pour créer de nouvelles pages. Par défaut, tous les templates sont sélectionnés pour le menu. Affectez une séquence vide à ce paramètre pour n'avoir aucun template sélectionné par défaut. Séquence des sous-classes de ``Page`` au format ``app_label.model_name``. Détermine l'ordre des éléments de la liste déroulante d'ajout de nouvelles pages dans l'interface d'administration. Une séquence de templates utilisé pour la balise de templates ``page_menu``. Chaque élément de cette séquence est une séquence de trois éléments contenant : un identifiant unique pour le template, un nom lui correspondant et le chemin d'accès au template. Ces templates seront alors accessibles comme choix pour définir dans quels menus une page peut apparaître. Notez que si un template pour menu est utilisé mais n'apparaît pas dans ce paramètre, toutes les pages y apparaîtront. Ajouter Une erreur est survenue sur la classe suivante. Est elle une sous classe directe de Page ?  Pied de page Accueil Si ``vrai``, les pages avec l'option ``login_required`` activée seront toujours visibles dans les menus et les résultats de recherche pour les utilisateurs non identifiés. Indépendamment de ce paramètre, un utilisateur non identifiés souhaitant visualiser une page avec l'option ``login_required`` activée sera redirigé vers la page d'authentification. Si coché, seuls les utilisateurs identifiés pourront voir la page Menu arborescent sur la gauche Lien Liens Identification obligatoire Page Pages Page de texte riche Pages de texte riche Afficher dans les menus Barre de navigation en haut de la page 