"use strict";(self["webpackChunkbuaa_hzt"]=self["webpackChunkbuaa_hzt"]||[]).push([[412],{9412:function(e,t,a){a.r(t),a.d(t,{default:function(){return p}});var n=a(641),l=a(4593),s=a(3813),r=a(6756),i=a(5526);function o(e,t,a,o,d,u){return(0,n.uX)(),(0,n.Wv)(s.I,{fluid:""},{default:(0,n.k6)((()=>[(0,n.bF)(r.L,{justify:"end",align:"center"},{default:(0,n.k6)((()=>[(0,n.bF)(i.B,{cols:"2"},{default:(0,n.k6)((()=>[(0,n.bF)(l.J,{color:"blue lighten-4",class:"pa-5",style:{height:"300px"}},{default:(0,n.k6)((()=>t[0]||(t[0]=[(0,n.Lk)("div",{class:"text-center"},"Centered Box 1",-1)]))),_:1})])),_:1}),(0,n.bF)(i.B,{cols:"2"},{default:(0,n.k6)((()=>[(0,n.bF)(l.J,{color:"green lighten-4",class:"pa-5"},{default:(0,n.k6)((()=>t[1]||(t[1]=[(0,n.Lk)("div",{class:"text-center"},"Centered Box 2",-1)]))),_:1})])),_:1}),(0,n.bF)(i.B,{cols:"2"},{default:(0,n.k6)((()=>[(0,n.bF)(l.J,{color:"green lighten-4",class:"pa-5"},{default:(0,n.k6)((()=>t[2]||(t[2]=[(0,n.Lk)("div",{class:"text-center"},"Centered Box 2",-1)]))),_:1})])),_:1})])),_:1})])),_:1})}var d={name:"SimpleLayoutDemo"},u=a(6262);const c=(0,u.A)(d,[["render",o]]);var p=c},3416:function(e,t,a){a.d(t,{y:function(){return k}});var n=a(641),l=a(7852),s=a(9669),r=a(5126),i=a(9923),o=a(9262),d=a(2191),u=a(5965),c=a(3240),p=a(3378),v=a(4663),f=a(7664),y=a(2428),b=a(4587),g=a(1247),m=a(4600);const C=(0,b.j)({start:Boolean,end:Boolean,icon:u.TX,image:String,text:String,...(0,i.r)(),...(0,o.u)(),...(0,d.r)(),...(0,c.S)(),...(0,p.k)(),...(0,v.X)(),...(0,f.yx)(),...(0,y.gI)({variant:"flat"})},"VAvatar"),k=(0,g.RW)()({name:"VAvatar",props:C(),setup(e,t){let{slots:a}=t;const{themeClasses:o}=(0,f.NX)(e),{borderClasses:u}=(0,i.M)(e),{colorClasses:v,colorStyles:b,variantClasses:g}=(0,y.rn)(e),{densityClasses:C}=(0,d.Q)(e),{roundedClasses:k}=(0,c.v)(e),{sizeClasses:S,sizeStyles:F}=(0,p.X)(e);return(0,m.C)((()=>(0,n.bF)(e.tag,{class:["v-avatar",{"v-avatar--start":e.start,"v-avatar--end":e.end},o.value,u.value,v.value,C.value,k.value,S.value,g.value,e.class],style:[b.value,F.value,e.style]},{default:()=>[a.default?(0,n.bF)(l.K,{key:"content-defaults",defaults:{VImg:{cover:!0,src:e.image},VIcon:{icon:e.icon}}},{default:()=>[a.default()]}):e.image?(0,n.bF)(r.y,{key:"image",src:e.image,alt:"",cover:!0},null):e.icon?(0,n.bF)(s.w,{key:"icon",icon:e.icon},null):e.text,(0,y.wN)(!1,"v-avatar")]}))),{}}})},4593:function(e,t,a){a.d(t,{J:function(){return X}});var n=a(641),l=a(3745),s=a(5832),r=a(1606),i=a(3416),o=a(7852),d=a(9669),u=a(9262),c=a(2191),p=a(5965),v=a(4587),f=a(1247),y=a(4600);const b=(0,v.j)({appendAvatar:String,appendIcon:p.TX,prependAvatar:String,prependIcon:p.TX,subtitle:[String,Number],title:[String,Number],...(0,u.u)(),...(0,c.r)()},"VCardItem"),g=(0,f.RW)()({name:"VCardItem",props:b(),setup(e,t){let{slots:a}=t;return(0,y.C)((()=>{const t=!(!e.prependAvatar&&!e.prependIcon),l=!(!t&&!a.prepend),u=!(!e.appendAvatar&&!e.appendIcon),c=!(!u&&!a.append),p=!(null==e.title&&!a.title),v=!(null==e.subtitle&&!a.subtitle);return(0,n.bF)("div",{class:["v-card-item",e.class],style:e.style},[l&&(0,n.bF)("div",{key:"prepend",class:"v-card-item__prepend"},[a.prepend?(0,n.bF)(o.K,{key:"prepend-defaults",disabled:!t,defaults:{VAvatar:{density:e.density,image:e.prependAvatar},VIcon:{density:e.density,icon:e.prependIcon}}},a.prepend):(0,n.bF)(n.FK,null,[e.prependAvatar&&(0,n.bF)(i.y,{key:"prepend-avatar",density:e.density,image:e.prependAvatar},null),e.prependIcon&&(0,n.bF)(d.w,{key:"prepend-icon",density:e.density,icon:e.prependIcon},null)])]),(0,n.bF)("div",{class:"v-card-item__content"},[p&&(0,n.bF)(r.r,{key:"title"},{default:()=>[a.title?.()??e.title]}),v&&(0,n.bF)(s.Z,{key:"subtitle"},{default:()=>[a.subtitle?.()??e.subtitle]}),a.default?.()]),c&&(0,n.bF)("div",{key:"append",class:"v-card-item__append"},[a.append?(0,n.bF)(o.K,{key:"append-defaults",disabled:!u,defaults:{VAvatar:{density:e.density,image:e.appendAvatar},VIcon:{density:e.density,icon:e.appendIcon}}},a.append):(0,n.bF)(n.FK,null,[e.appendIcon&&(0,n.bF)(d.w,{key:"append-icon",density:e.density,icon:e.appendIcon},null),e.appendAvatar&&(0,n.bF)(i.y,{key:"append-avatar",density:e.density,image:e.appendAvatar},null)])])])})),{}}});var m=a(697),C=a(5126),k=a(9923),S=a(2542),F=a(7018),h=a(9296),I=a(9788),j=a(8184),A=a(3240),x=a(6314),V=a(4663),B=a(7664),N=a(2428),_=a(759);const w=(0,v.j)({appendAvatar:String,appendIcon:p.TX,disabled:Boolean,flat:Boolean,hover:Boolean,image:String,link:{type:Boolean,default:void 0},prependAvatar:String,prependIcon:p.TX,ripple:{type:[Boolean,Object],default:!0},subtitle:[String,Number],text:[String,Number],title:[String,Number],...(0,k.r)(),...(0,u.u)(),...(0,c.r)(),...(0,S.X)(),...(0,F.s)(),...(0,h.gi)(),...(0,I.M)(),...(0,j.S)(),...(0,A.S)(),...(0,x.WC)(),...(0,V.X)(),...(0,B.yx)(),...(0,N.gI)({variant:"elevated"})},"VCard"),X=(0,f.RW)()({name:"VCard",directives:{Ripple:_.n},props:w(),setup(e,t){let{attrs:a,slots:s}=t;const{themeClasses:r}=(0,B.NX)(e),{borderClasses:i}=(0,k.M)(e),{colorClasses:d,colorStyles:u,variantClasses:p}=(0,N.rn)(e),{densityClasses:v}=(0,c.Q)(e),{dimensionStyles:f}=(0,S.S)(e),{elevationClasses:b}=(0,F.j)(e),{loaderClasses:V}=(0,h.pn)(e),{locationStyles:_}=(0,I.z)(e),{positionClasses:w}=(0,j.J)(e),{roundedClasses:X}=(0,A.v)(e),W=(0,x.iE)(e,a),R=(0,n.EW)((()=>!1!==e.link&&W.isLink.value)),$=(0,n.EW)((()=>!e.disabled&&!1!==e.link&&(e.link||W.isClickable.value)));return(0,y.C)((()=>{const t=R.value?"a":e.tag,a=!(!s.title&&null==e.title),c=!(!s.subtitle&&null==e.subtitle),y=a||c,k=!!(s.append||e.appendAvatar||e.appendIcon),S=!!(s.prepend||e.prependAvatar||e.prependIcon),F=!(!s.image&&!e.image),I=y||S||k,j=!(!s.text&&null==e.text);return(0,n.bo)((0,n.bF)(t,(0,n.v6)({class:["v-card",{"v-card--disabled":e.disabled,"v-card--flat":e.flat,"v-card--hover":e.hover&&!(e.disabled||e.flat),"v-card--link":$.value},r.value,i.value,d.value,v.value,b.value,V.value,w.value,X.value,p.value,e.class],style:[u.value,f.value,_.value,e.style],onClick:$.value&&W.navigate,tabindex:e.disabled?-1:void 0},W.linkProps),{default:()=>[F&&(0,n.bF)("div",{key:"image",class:"v-card__image"},[s.image?(0,n.bF)(o.K,{key:"image-defaults",disabled:!e.image,defaults:{VImg:{cover:!0,src:e.image}}},s.image):(0,n.bF)(C.y,{key:"image-img",cover:!0,src:e.image},null)]),(0,n.bF)(h.E2,{name:"v-card",active:!!e.loading,color:"boolean"===typeof e.loading?void 0:e.loading},{default:s.loader}),I&&(0,n.bF)(g,{key:"item",prependAvatar:e.prependAvatar,prependIcon:e.prependIcon,title:e.title,subtitle:e.subtitle,appendAvatar:e.appendAvatar,appendIcon:e.appendIcon},{default:s.item,prepend:s.prepend,title:s.title,subtitle:s.subtitle,append:s.append}),j&&(0,n.bF)(m.O,{key:"text"},{default:()=>[s.text?.()??e.text]}),s.default?.(),s.actions&&(0,n.bF)(l.S,null,{default:s.actions}),(0,N.wN)($.value,"v-card")]}),[[(0,n.gN)("ripple"),$.value&&e.ripple]])})),{}}})},3745:function(e,t,a){a.d(t,{S:function(){return o}});var n=a(641),l=a(9262),s=a(2858),r=a(1247),i=a(4600);const o=(0,r.RW)()({name:"VCardActions",props:(0,l.u)(),setup(e,t){let{slots:a}=t;return(0,s.Uh)({VBtn:{slim:!0,variant:"text"}}),(0,i.C)((()=>(0,n.bF)("div",{class:["v-card-actions",e.class],style:e.style},[a.default?.()]))),{}}})},5832:function(e,t,a){a.d(t,{Z:function(){return u}});var n=a(641),l=a(9262),s=a(4663),r=a(4587),i=a(1247),o=a(4600);const d=(0,r.j)({opacity:[Number,String],...(0,l.u)(),...(0,s.X)()},"VCardSubtitle"),u=(0,i.RW)()({name:"VCardSubtitle",props:d(),setup(e,t){let{slots:a}=t;return(0,o.C)((()=>(0,n.bF)(e.tag,{class:["v-card-subtitle",e.class],style:[{"--v-card-subtitle-opacity":e.opacity},e.style]},a))),{}}})},697:function(e,t,a){a.d(t,{O:function(){return u}});var n=a(641),l=a(9262),s=a(4663),r=a(4587),i=a(1247),o=a(4600);const d=(0,r.j)({opacity:[Number,String],...(0,l.u)(),...(0,s.X)()},"VCardText"),u=(0,i.RW)()({name:"VCardText",props:d(),setup(e,t){let{slots:a}=t;return(0,o.C)((()=>(0,n.bF)(e.tag,{class:["v-card-text",e.class],style:[{"--v-card-text-opacity":e.opacity},e.style]},a))),{}}})},1606:function(e,t,a){a.d(t,{r:function(){return l}});var n=a(2586);const l=(0,n.G)("v-card-title")},5526:function(e,t,a){a.d(t,{B:function(){return g}});a(4114),a(8992),a(3949),a(8872),a(5792);var n=a(9262),l=a(8353),s=a(4663),r=a(33),i=a(641),o=a(4587),d=a(1247);const u=(()=>l.fi.reduce(((e,t)=>(e[t]={type:[Boolean,String,Number],default:!1},e)),{}))(),c=(()=>l.fi.reduce(((e,t)=>{const a="offset"+(0,r.ZH)(t);return e[a]={type:[String,Number],default:null},e}),{}))(),p=(()=>l.fi.reduce(((e,t)=>{const a="order"+(0,r.ZH)(t);return e[a]={type:[String,Number],default:null},e}),{}))(),v={col:Object.keys(u),offset:Object.keys(c),order:Object.keys(p)};function f(e,t,a){let n=e;if(null!=a&&!1!==a){if(t){const a=t.replace(e,"");n+=`-${a}`}return"col"===e&&(n="v-"+n),"col"!==e||""!==a&&!0!==a?(n+=`-${a}`,n.toLowerCase()):n.toLowerCase()}}const y=["auto","start","end","center","baseline","stretch"],b=(0,o.j)({cols:{type:[Boolean,String,Number],default:!1},...u,offset:{type:[String,Number],default:null},...c,order:{type:[String,Number],default:null},...p,alignSelf:{type:String,default:null,validator:e=>y.includes(e)},...(0,n.u)(),...(0,s.X)()},"VCol"),g=(0,d.RW)()({name:"VCol",props:b(),setup(e,t){let{slots:a}=t;const n=(0,i.EW)((()=>{const t=[];let a;for(a in v)v[a].forEach((n=>{const l=e[n],s=f(a,n,l);s&&t.push(s)}));const n=t.some((e=>e.startsWith("v-col-")));return t.push({"v-col":!n||!e.cols,[`v-col-${e.cols}`]:e.cols,[`offset-${e.offset}`]:e.offset,[`order-${e.order}`]:e.order,[`align-self-${e.alignSelf}`]:e.alignSelf}),t}));return()=>(0,i.h)(e.tag,{class:[n.value,e.class],style:e.style},a.default?.())}})},6756:function(e,t,a){a.d(t,{L:function(){return A}});a(4114),a(8992),a(3949),a(8872),a(5792);var n=a(9262),l=a(8353),s=a(4663),r=a(33),i=a(641),o=a(4587),d=a(1247);const u=["start","end","center"],c=["space-between","space-around","space-evenly"];function p(e,t){return l.fi.reduce(((a,n)=>{const l=e+(0,r.ZH)(n);return a[l]=t(),a}),{})}const v=[...u,"baseline","stretch"],f=e=>v.includes(e),y=p("align",(()=>({type:String,default:null,validator:f}))),b=[...u,...c],g=e=>b.includes(e),m=p("justify",(()=>({type:String,default:null,validator:g}))),C=[...u,...c,"stretch"],k=e=>C.includes(e),S=p("alignContent",(()=>({type:String,default:null,validator:k}))),F={align:Object.keys(y),justify:Object.keys(m),alignContent:Object.keys(S)},h={align:"align",justify:"justify",alignContent:"align-content"};function I(e,t,a){let n=h[e];if(null!=a){if(t){const a=t.replace(e,"");n+=`-${a}`}return n+=`-${a}`,n.toLowerCase()}}const j=(0,o.j)({dense:Boolean,noGutters:Boolean,align:{type:String,default:null,validator:f},...y,justify:{type:String,default:null,validator:g},...m,alignContent:{type:String,default:null,validator:k},...S,...(0,n.u)(),...(0,s.X)()},"VRow"),A=(0,d.RW)()({name:"VRow",props:j(),setup(e,t){let{slots:a}=t;const n=(0,i.EW)((()=>{const t=[];let a;for(a in F)F[a].forEach((n=>{const l=e[n],s=I(a,n,l);s&&t.push(s)}));return t.push({"v-row--no-gutters":e.noGutters,"v-row--dense":e.dense,[`align-${e.align}`]:e.align,[`justify-${e.justify}`]:e.justify,[`align-content-${e.alignContent}`]:e.alignContent}),t}));return()=>(0,i.h)(e.tag,{class:["v-row",n.value,e.class],style:e.style},a.default?.())}})}}]);
//# sourceMappingURL=412.cb2e7c62.js.map