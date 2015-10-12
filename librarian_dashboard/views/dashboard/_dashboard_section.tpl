<%def name="plugin(name, heading, extra_classes, taborder)">
    <section class="dashboard-section o-collapsible-section o-collapsed ${extra_classes}" id="dashboard-${name}">
    <h2 class="o-collapsible-section-title" id="dashboard-${name}-header" tabindex="${taborder}" role="button" aria-controls="dashboard-${name}-panel">    
        <span class="icon"></span>
        ${heading}
    </h2>
    <div class="dash-section-content o-collapsible-section-panel" id="dashboard-${name}-panel" tabindex>
        ${caller.body()}
    </div>
    </section>
</%def>
