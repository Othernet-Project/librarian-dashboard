<%def name="plugin(name, heading, extra_classes)">
    <section class="dashboard-section o-collapsible-section o-collapsed ${extra_classes}" id="dashboard-${name}">
    <h2 class="o-collapsible-section-title">    
        <span class="icon"></span>
        ${heading}
    </h2>
    <div class="dash-section-content o-collapsible-section-panel">
        ${caller.body()}
    </div>
    </section>
</%def>
